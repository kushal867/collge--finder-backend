import requests
from django.conf import settings
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from college.models import College, Student, Parent, Favorite, User, Course, Review
from college.api.serializers import (
    StudentSerializer, ParentSerializer, FavoriteSerializer, UserSerializer,
    CollegeSerializer, CourseSerializer, ReviewSerializer
)

# Ollama API URL
OLLAMA_API_URL = getattr(settings, 'OLLAMA_API_URL', 'http://localhost:11434/api/generate')


# ---------- Ollama Service ----------
def generate_college_comparison(colleges, preferences):
    """Generate comparison using Ollama AI."""
    college_descriptions = []
    for c in colleges:
        courses = ', '.join(course.name for course in c.courses.all())
        college_descriptions.append(
            f"{c.name}, {getattr(c, 'location', '')}, Courses: {courses}, "
            f"Budget: {c.budget}, Facilities: {c.facilities}"
        )

    prompt = (
        f"Compare the following colleges for a student with these preferences: {preferences}\n\n"
        + "\n".join(college_descriptions)
        + "\n\nWhich college(s) would be the best fit and why?"
    )

    response = requests.post(OLLAMA_API_URL, json={"model": "llama3.2", "prompt": prompt})

    # Safely parse JSON or return raw text
    try:
        return response.json().get("response", "")
    except ValueError:
        return response.text  # Return plain text if JSON parsing fails


# ---------- Custom API ----------
@api_view(['POST'])
def compare_colleges_ollama(request):
    """Compare colleges using Ollama AI."""
    college_ids = request.data.get('college_ids', [])
    preferences = request.data.get('preferences', '')

    if not college_ids:
        return Response({'error': 'college_ids is required'}, status=status.HTTP_400_BAD_REQUEST)

    colleges = College.objects.filter(id__in=college_ids)
    if not colleges.exists():
        return Response({'error': 'No colleges found for the given IDs'}, status=status.HTTP_404_NOT_FOUND)

    try:
        ollama_result = generate_college_comparison(colleges, preferences)
        if ollama_result:
            return Response({"ollama_response": ollama_result}, status=status.HTTP_200_OK)
        return Response({"error": "Ollama API error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# ---------- Generic CRUD Function-Based Views ----------
def list_create_view(model, serializer_class):
    """Return a view for listing and creating objects."""
    @api_view(['GET', 'POST'])
    def view(request):
        if request.method == 'GET':
            objects = model.objects.all()
            serializer = serializer_class(objects, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        elif request.method == 'POST':
            serializer = serializer_class(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'message': f'{model.__name__} created successfully'}, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return view


def detail_view(model, serializer_class):
    """Return a view for retrieve, update, and delete."""
    @api_view(['GET', 'PUT', 'DELETE'])
    def view(request, id):
        try:
            obj = model.objects.get(id=id)
        except model.DoesNotExist:
            return Response({'error': f'{model.__name__} not found'}, status=status.HTTP_404_NOT_FOUND)

        if request.method == 'GET':
            serializer = serializer_class(obj)
            return Response(serializer.data, status=status.HTTP_200_OK)
        elif request.method == 'PUT':
            serializer = serializer_class(obj, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({'message': f'{model.__name__} updated successfully'}, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        elif request.method == 'DELETE':
            obj.delete()
            return Response({'message': f'{model.__name__} deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
    return view


# ---------- Register Views ----------
college_list_create = list_create_view(College, CollegeSerializer)
college_detail = detail_view(College, CollegeSerializer)

course_list_create = list_create_view(Course, CourseSerializer)
course_detail = detail_view(Course, CourseSerializer)

review_list_create = list_create_view(Review, ReviewSerializer)
review_detail = detail_view(Review, ReviewSerializer)

student_list_create = list_create_view(Student, StudentSerializer)
student_detail = detail_view(Student, StudentSerializer)

parent_list_create = list_create_view(Parent, ParentSerializer)
parent_detail = detail_view(Parent, ParentSerializer)

favorite_list_create = list_create_view(Favorite, FavoriteSerializer)
favorite_detail = detail_view(Favorite, FavoriteSerializer)

user_list_create = list_create_view(User, UserSerializer)
user_detail = detail_view(User, UserSerializer)
