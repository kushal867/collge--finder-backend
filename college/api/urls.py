
from django.urls import path
from .views import college_list_create, course_list_create, review_list_create, student_list_create, parent_list_create, favorite_list_create, user_list_create

urlpatterns = [
    path('colleges/', college_list_create, name='college-list-create'),
    path('courses/', course_list_create, name='course-list-create'),
    path('reviews/', review_list_create, name='review-list-create'),
    path('students/', student_list_create, name='student-list-create'),
    path('parents/', parent_list_create, name='parent-list-create'),
    path('favorites/', favorite_list_create, name='favorite-list-create'),
    path('users/', user_list_create, name='user-list-create'),
]
