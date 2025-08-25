
from django.db import models
from django.contrib.auth.models import AbstractUser

# Custom User model
class User(AbstractUser):
	email = models.EmailField(unique=True)

# Student model
class Student(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	name = models.CharField(max_length=100)
	gpa_obtained = models.DecimalField(max_digits=4, decimal_places=2)
	location = models.CharField(max_length=100)
	phone_number = models.CharField(max_length=20)
	email = models.EmailField()
	interest_colleges = models.TextField(blank=True)

	def __str__(self):
		return self.name

# Parent model
class Parent(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	name = models.CharField(max_length=100)
	student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='parents')
	location = models.CharField(max_length=100)
	budget = models.DecimalField(max_digits=10, decimal_places=2)

	def __str__(self):
		return self.name

# College model
class College(models.Model):
	name = models.CharField(max_length=200)
	affiliation = models.CharField(max_length=200)
	courses = models.ManyToManyField('Course', related_name='colleges')
	budget = models.DecimalField(max_digits=10, decimal_places=2)
	facilities = models.TextField(blank=True)

	def __str__(self):
		return self.name

# Course model
class Course(models.Model):
	name = models.CharField(max_length=200)
	objectives = models.TextField(blank=True)
	advantages = models.TextField(blank=True)

	def __str__(self):
		return self.name

# Favorite model
class Favorite(models.Model):
	student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='favorites')
	college = models.ForeignKey(College, on_delete=models.CASCADE, related_name='favorited_by')
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f"{self.student.name} - {self.college.name}"

# Review model
class Review(models.Model):
	student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='reviews')
	college = models.ForeignKey(College, on_delete=models.CASCADE, related_name='reviews')
	rating = models.PositiveSmallIntegerField()
	comment = models.TextField(blank=True)
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f"{self.college.name} - {self.rating}"
