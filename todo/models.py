from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.TextField()

class Task(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.TextField()
    description = models.TextField()
    category = models.ForeignKey(Category)

class CategoryTaskMap(models.Model):
	id = models.AutoField(primary_key=True)
	user = models.ForeignKey(User)
	category = models.ForeignKey(Category)
	task = models.ForeignKey(Task)
	
