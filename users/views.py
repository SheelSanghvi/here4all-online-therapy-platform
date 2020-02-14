from django.shortcuts import render, redirect
from django.contrib.auth.models import User 
from .forms import *
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from .models import *

#paginator
from django.core.paginator import Paginator


#rest framework imports
from rest_framework.settings import api_settings
from .serializers import *
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.views import APIView
from rest_framework import generics, mixins
from rest_framework.mixins import ListModelMixin


def home(request):
	return render(request, "users/homepage.html")

def whytherapy(request):
	return render(request, "users/whytherapy.html")

def ourteam(request):
	therapist= User.objects.filter(user_type=2)
	return render(request, "users/ourteam.html", {'therapist':therapist})

def blogs(request):
	topics = Blogs.TOPICS
	blogs = Blogs.objects.all()

	paginator= Paginator(blogs, 2)
	page = request.GET.get('page')
	blogs = paginator.get_page(page)

	return render(request, "users/blogs.html", {'topic': None, 'topics': topics, 'blogs': blogs})

def topicBlogs(request, url_topic):
	topics = Blogs.TOPICS
	for t in Blogs.TOPICS:
		if t[1]== url_topic:
			blogs= Blogs.objects.filter(topic=t[0])
	return render(request, "users/topicBlogs.html", {'url_topic': url_topic, 'topics': topics, 'blogs': blogs})

def register(request):
	if request.method == 'POST':
		form = RegistrationForm(request.POST)
		if form.is_valid():
			user=form.save()
			user.set_password(user.password)
			user.save()
			return redirect('login')
	else:
		form = RegistrationForm()
	return render(request, 'users/register.html', {'form': form})

def login(request):
	return render(request, 'users/login.html')

def deleteAccount(request):
	id = User.objects.get(id= request.user.id)
	id.delete()
	return redirect('home')

@login_required
def dashboard(request):
	if request.user.user_type =='2':
		if request.method== 'POST':			
			form1= UserUpdate(request.POST, request.FILES, instance=request.user)
			if form1.is_valid():
				form1.save()
		else:
			form1= UserUpdate(instance=request.user)

		therapist= User.objects.get(id=request.user.id)
		return render(request, 'users/therapistDashboardProfile.html', {'therapist': therapist, 'form1': form1})
	else:
		if request.method== 'POST':			
			form1= UserUpdate(request.POST, request.FILES, instance=request.user)
			if form1.is_valid():
				form1.save()
		else:
			form1= UserUpdate(instance=request.user)
		patient= User.objects.get(id=request.user.id)
		return render(request, 'users/patientDashboardProfile.html', {'patient': patient, 'form1': form1})

@login_required
def therapistDashboardBlogs(request):
	if request.user.user_type == '1':
		return redirect('dashboard')
	therapistblogs= Blogs.objects.filter(therapist_id= request.user.id)
	if request.method == 'POST':
		form= BlogsForm(request.POST, request.FILES)
		if form.is_valid():
			post=form.save(commit=False)
			post.therapist_id = request.user
			post.save()
			return render(request, 'users/therapistDashboardBlogs.html', {'form': BlogsForm(), 'blogstatus': True, 'therapistblogs': therapistblogs})
	
	else:
		form= BlogsForm()
		return render(request, 'users/therapistDashboardBlogs.html', {'form': BlogsForm(), 'blogstatus': False, 'therapistblogs': therapistblogs})

@login_required
def therapistDashboardChat(request):
	therapist = User.objects.get(id=request.user.id)
	xx = Question.objects.filter(therapist=request.user.id)
	pending = 0
	solved = 0
	for x in xx:
		if x.answer == "Reply Pending":
			pending += 1
		else:
			solved +=1
	if request.method == "POST":
		ans = request.POST['solution']
		qid = request.POST['qid']
		obj = Question.objects.get(id= qid)
		obj.answer = ans
		obj.save()
	conversation = Question.objects.filter(therapist=request.user.id).order_by('-time_stamp')
	total = solved + pending
	if total != 0:
		ratio = solved/total
	else:
		ratio=0
	return render(request, 'users/therapistDashboardChat.html', {'conversation': conversation, 'solved': solved, 'pending': pending, 'total': total, 'ratio': ratio, 'therapist': therapist})

@login_required
def patientDashboardChat(request):
	users= User.objects.filter(user_type=2)
	current_patient = int(request.user.id)	
	conversation = Question.objects.filter(patient_id=current_patient).order_by('-time_stamp')
	if request.method == 'POST':
		therapist = int(request.POST['therapist'])
		ques = request.POST['Issue']
		Question.objects.create(patient_id=current_patient, therapist_id=therapist, question=ques)
	return render(request, 'users/patientDashboardChat.html', {'therapists': users, 'conversation': conversation})


def guestContactUs(request):
	if request.method =='POST':
		form = GuestContactUsForm(request.POST)
		if form.is_valid():
			user=form.save()
			return render(request, 'users/contact.html', {'form': GuestContactUsForm(), 'successmessage': True})
			# html = "<html><body><p> Thankyou for contacting us!</p></body></html>"
			# return HttpResponse('Thankyou for contacting us!')

	form= GuestContactUsForm()
	return render(request, 'users/contact.html', {'form': GuestContactUsForm(), 'successmessage': False})




#rest framework views

class BlogsAPIView(generics.ListAPIView, mixins.CreateModelMixin):
	permission_classes = [AllowAny]
	queryset = Blogs.objects.all()
	serializer_class = BlogsSerializer

	def post(self, request, *args, **kwargs):
		return self.create(request, *args, **kwargs)

class BlogsRudView(generics.RetrieveUpdateDestroyAPIView):
	permission_classes = [AllowAny]
	lookup_field= 'id'
	queryset = Blogs.objects.all()
	serializer_class = BlogsSerializer

class GuestContactUsAPIView(generics.ListAPIView, mixins.CreateModelMixin):
	permission_classes = [IsAuthenticated]
	queryset = GuestContactUs.objects.all()
	serializer_class= GuestContactUsSerializer
	def post(self, request, *args, **kwargs):
		return self.create(request, *args, **kwargs)

class GuestContactUsRudView(generics.RetrieveUpdateDestroyAPIView):
	permission_classes =  [IsAuthenticated]
	lookup_field= 'email'
	queryset =  GuestContactUs.objects.all()
	serializer_class= GuestContactUsSerializer

class UserAPIView(generics.ListAPIView, mixins.CreateModelMixin):
	permission_classes = [IsAuthenticated]
	queryset = User.objects.all()
	serializer_class= UserSerializer
	def post(self, request, *args, **kwargs):
		return self.create(request, *args, **kwargs)

class UserRudView(generics.RetrieveUpdateDestroyAPIView):
	permission_classes =  [IsAuthenticated]
	lookup_field= 'id'
	queryset =  User.objects.all()
	serializer_class= UserSerializer

class FavouriteBlogView(generics.GenericAPIView):
	permission_classes = [IsAuthenticated]

	def get(self, request, *args, **kwargs):
		blog = Blogs.objects.get(id=kwargs['id'])
		blog.favourited_by.add(request.user)
		return JsonResponse(BlogsSerializer(blog).data)


# my_json_response = fetch('http://localhost:8000/api/blogs', method="POST", headers={'Authentication': "Token 38u79238htjmaskl"}, body="")