from django.contrib import admin

# Register your models here.
from .models import Job,JobRequests

admin.site.register(Job)
admin.site.register(JobRequests)