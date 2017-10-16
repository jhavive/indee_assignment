from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,logout
from django.contrib.auth.models import User
from django.template import loader
from django.http import HttpResponse
import models,json
from rest_framework.response import Response
from rest_framework.views import APIView

class Login(APIView):

	def get(self, request, format=None):
		return render(request, 'app/login.html',)

	def post(self, request, format=None):
		print request
		user = authenticate(username=request.POST.get('username'), password=request.POST.get('password'))
		if user is not None:
		    return redirect("/category")
		return render(request, 'app/login.html',)

def logout_view(request):
	logout(request)
	return redirect("/")
	
class CreateUser(APIView):

	def get(self, request, format=None):
		return render(request, 'app/signup.html',)

	def post(self, request, format=None):
		user = User.objects.create_user(request.POST.get('username'),'',request.POST.get('password'))
		if user is not None:
			print "abc"
			return redirect("/category")
		return render(request, 'app/signup.html',)

class Category(APIView):

	def get(self, request, format=None):
		categories = models.Category.objects.all()
		tasks = models.Task.objects.all()
		return render(request, 'app/home.html',{'categories':categories,'tasks':tasks})

	def post(self, request, format=None):
		if request.POST.get("description") is None:
			print request.POST.get("title")
			category = models.Category(title=request.POST.get("title"))
			category.save()

		else:
			print request.POST.get("category_id")
			category_id = request.POST.get("category_id")
			category_found = models.Category.objects.get(id=category_id)
			task = models.Task(title=request.POST.get("title"),
				description=request.POST.get("description"),
				category= category_found)
			task.save()
		categories = models.Category.objects.all()
		tasks = models.Task.objects.all()
		return render(request, 'app/home.html',{'categories':categories,'tasks':tasks})
