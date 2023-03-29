
from django.db import models 
from django.contrib.auth.models import User


class AddJob(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=300)
    description = models.TextField(max_length=500)
    location = models.CharField(max_length=150)
    type = models.CharField( max_length=10)
    category = models.CharField(max_length=100)
    last_date = models.DateTimeField()
    company_name = models.CharField(max_length=100)
    website = models.CharField(max_length=100, default="")
    job_photo = models.ImageField(upload_to="static/images",null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    def str(self):
        return self.title
    

