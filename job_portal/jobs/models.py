from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Job(models.Model):
    job_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100,null=True,blank=True)
    company_name = models.CharField(max_length=100,null=True,blank=True)
    description = models.TextField(null=True,blank=True)
    salary = models.IntegerField()
    created_by = models.CharField(max_length=100,null=True,blank=True)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return "%s"% self.title


class JobRequests(models.Model):
    request_on = models.ManyToManyField(Job,blank=True)
    request_by = models.CharField(max_length=100,null=True,blank=True)
    request_at = models.DateTimeField(auto_now=False,auto_now_add=True)

    def __str__(self):
        return "%s"%self.request_by

