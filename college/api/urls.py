from django.urls import path
from .views import (
    college_list_create, college_detail,
    course_list_create, course_detail,
    review_list_create, review_detail,
    student_list_create, student_detail,
    parent_list_create, parent_detail,
    favorite_list_create, favorite_detail,
    user_list_create, user_detail,
    compare_colleges_ollama
)

urlpatterns = [
    # Custom AI comparison
    path('compare-ollama/', compare_colleges_ollama, name='compare-colleges-ollama'),

    # College
    path('colleges/', college_list_create, name='college-list-create'),
    path('colleges/<int:id>/', college_detail, name='college-detail'),

    # Course
    path('courses/', course_list_create, name='course-list-create'),
    path('courses/<int:id>/', course_detail, name='course-detail'),

    # Review
    path('reviews/', review_list_create, name='review-list-create'),
    path('reviews/<int:id>/', review_detail, name='review-detail'),

    # Student
    path('students/', student_list_create, name='student-list-create'),
    path('students/<int:id>/', student_detail, name='student-detail'),

    # Parent
    path('parents/', parent_list_create, name='parent-list-create'),
    path('parents/<int:id>/', parent_detail, name='parent-detail'),

    # Favorite
    path('favorites/', favorite_list_create, name='favorite-list-create'),
    path('favorites/<int:id>/', favorite_detail, name='favorite-detail'),

    # User
    path('users/', user_list_create, name='user-list-create'),
    path('users/<int:id>/', user_detail, name='user-detail'),
]
