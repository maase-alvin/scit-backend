"""
Database models.
"""
import uuid
import os

from django.conf import settings
from django.db import models
from django.contrib.auth.models import (
AbstractBaseUser, 
 BaseUserManager,
 PermissionsMixin )
# Create your models here.

def programme_image_file_path(instance, filename):
    """Generate file path for new program image"""
    ext = os.path.splitext(filename)[1] # get extension
    filename = f'{uuid.uuid4()}{ext}' # generate filename
    return os.path.join('uploads', 'programme', filename) # return path

def academic_activities_image_file_path(instance, filename):
    """Generate file path for new academic activities image"""
    ext = os.path.splitext(filename)[1] # get extension
    filename = f'{uuid.uuid4()}{ext}' # generate filename
    return os.path.join('uploads', 'academic_activities', filename) # return path


class UserManager(BaseUserManager):
    """Manager for user profiles"""
    def create_user(self, email, password=None, **extra_fields):
        """
        Create, save and return a new user
        """
        if not email:
            raise ValueError('User must have an email address')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        # user.set_password(password)
        user.set_password(password)
        user.save(using=self._db)

        return user
    
    def create_superuser(self, email, password):
        """
        Create and return a new superuser
        """
        user = self.create_user(email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user
    

class User(AbstractBaseUser, PermissionsMixin):
    """
    Custom user model that supports using email instead of username
    """
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True) # can login
    is_staff = models.BooleanField(default=False) # staff user
    profile = models.CharField(max_length=255, blank=True, null=True)

    objects = UserManager()

    USERNAME_FIELD = 'email' # username field
    # REQUIRED_FIELDS = ['name'] # required fields

    def __str__(self):
        return self.email


class School(models.Model):
    """
    School model
    """
    name = models.CharField(max_length=255)
    telephone = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    

class Programme(models.Model):
    """
    Program Model
    """
    name = models.CharField(max_length=255)
    duration = models.CharField(max_length=255)
    cost = models.IntegerField()
    description = models.CharField(max_length=255)
    image = models.ImageField(null=True, upload_to=programme_image_file_path)

    def __str__(self):
        return self.name
    
    
class AcademicActivities(models.Model):
    """
    Academic Activities Model
    """
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    department = models.CharField(max_length=255)
    duration = models.CharField(max_length=255)
    amount = models.IntegerField()
    related_information = models.CharField(max_length=255)
    image = models.ImageField(null=True, upload_to=academic_activities_image_file_path)

    def __str__(self):
        return self.name
    
    
class Payment(models.Model):
    """Payments Model"""
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    programme = models.ForeignKey(Programme, on_delete=models.CASCADE, null=True, blank=True)
    academic_activities = models.ForeignKey(AcademicActivities, on_delete=models.CASCADE, null=True, blank=True)
    amount = models.IntegerField()
    method = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.user.email
    
    
class Application(models.Model):
    """Application"""
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    programme = models.ForeignKey(Programme, on_delete=models.CASCADE, null=True, blank=True)
    academic_activities = models.ForeignKey(AcademicActivities, on_delete=models.CASCADE, null=True, blank=True)
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE, null=True, blank=True)
    status = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.user.email
    
    

