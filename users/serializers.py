from django.conf import settings
from .models import *
from rest_framework import serializers

class BlogsSerializer(serializers.ModelSerializer):
	class Meta:
		model=Blogs
		fields='__all__'

class GuestContactUsSerializer(serializers.ModelSerializer):
	class Meta:
		model= GuestContactUs
		fields= '__all__'

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model= User
		fields= '__all__'