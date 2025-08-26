from django.contrib import admin
from .models import College,Course,Student,Parent,Favorite,Review,User
# Register your models here.
admin.site.register(College)
admin.site.register(Course)
admin.site.register(Student)
admin.site.register(Parent)
admin.site.register(Favorite)
admin.site.register(Review)
admin.site.register(User)
