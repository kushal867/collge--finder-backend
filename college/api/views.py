
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from college.api.serializers import StudentSerializer, ParentSerializer, FavoriteSerializer, UserSerializer, CollegeSerializer, CourseSerializer, ReviewSerializer
from college.models import Student, Parent, Favorite, User, College, Course, Review

# Student List and Create
@api_view(['GET', 'POST'])
def student_list_create(request):
	if request.method == 'GET':
		students = Student.objects.all()
		serializer = StudentSerializer(students, many=True)
		return Response(serializer.data, status=status.HTTP_200_OK)
	elif request.method == 'POST':
		serializer = StudentSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response({'message': 'Student created successfully'}, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Parent List and Create
@api_view(['GET', 'POST'])
def parent_list_create(request):
	if request.method == 'GET':
		parents = Parent.objects.all()
		serializer = ParentSerializer(parents, many=True)
		return Response(serializer.data, status=status.HTTP_200_OK)
	elif request.method == 'POST':
		serializer = ParentSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response({'message': 'Parent created successfully'}, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Favorite List and Create
@api_view(['GET', 'POST'])
def favorite_list_create(request):
	if request.method == 'GET':
		favorites = Favorite.objects.all()
		serializer = FavoriteSerializer(favorites, many=True)
		return Response(serializer.data, status=status.HTTP_200_OK)
	elif request.method == 'POST':
		serializer = FavoriteSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response({'message': 'Favorite created successfully'}, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# User List and Create
@api_view(['GET', 'POST'])
def user_list_create(request):
	if request.method == 'GET':
		users = User.objects.all()
		serializer = UserSerializer(users, many=True)
		return Response(serializer.data, status=status.HTTP_200_OK)
	elif request.method == 'POST':
		serializer = UserSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response({'message': 'User created successfully'}, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# College List and Create
@api_view(['GET', 'POST'])
def college_list_create(request):
	if request.method == 'GET':
		colleges = College.objects.all()
		serializer = CollegeSerializer(colleges, many=True)
		return Response(serializer.data, status=status.HTTP_200_OK)
	elif request.method == 'POST':
		serializer = CollegeSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response({'message': 'College created successfully'}, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Course List and Create
@api_view(['GET', 'POST'])
def course_list_create(request):
	if request.method == 'GET':
		courses = Course.objects.all()
		serializer = CourseSerializer(courses, many=True)
		return Response(serializer.data, status=status.HTTP_200_OK)
	elif request.method == 'POST':
		serializer = CourseSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response({'message': 'Course created successfully'}, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Review List and Create
@api_view(['GET', 'POST'])
def review_list_create(request):
	if request.method == 'GET':
		reviews = Review.objects.all()
		serializer = ReviewSerializer(reviews, many=True)
		return Response(serializer.data, status=status.HTTP_200_OK)
	elif request.method == 'POST':
		serializer = ReviewSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response({'message': 'Review created successfully'}, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
