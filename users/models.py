from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.conf import settings
from django.core.validators import RegexValidator



class UserManager(BaseUserManager):
	def create_user(self, email, password, **extra_fields):
		if not email:
			raise ValueError("Email required")
		if not password:
			raise ValuError("Password required")

		user=self.model(email=email, **extra_fields)
		user.set_password(password)
		user.save()
		return user

	def create_superuser(self,email, password): 
		user=self.create_user(email,password)
		user.is_staff=True
		user.is_superuser=True
		user.save()
		return user

class User(AbstractBaseUser, PermissionsMixin):
	USERTYPE=(
		('1','Patient'),
		('2','Therapist'),
		)
	GENDER=[('M','M'),('F','F'),('Transgender','Transgender')]
	email= models.EmailField(unique=True)
	user_type= models.CharField(max_length=10, choices=USERTYPE)
	f_name= models.CharField(max_length= 20)
	l_name= models.CharField(max_length= 20)
	age= models.IntegerField(blank=False, null=False, default=0)
	gender= models.CharField(choices= GENDER, max_length=15)
	phone_regex=RegexValidator(regex = r'^\+?1?\d{9,10}$' ,message='Phone number must be valid')
	phone= models.CharField(validators=[phone_regex], max_length=10, blank=True, null=True, default=None)
	additional_data=models.CharField(max_length=100, blank=True, null= True, default=None)
	image=models.ImageField(upload_to="profile_photo",blank=True, null=True, default="defaultpp.jpg")
	date_joined = models.DateTimeField(auto_now_add=True)
	is_staff= models.BooleanField(default=False)
	is_active= models.BooleanField(default=True)
	is_superuser= models.BooleanField(default=False)



	objects = UserManager()

	USERNAME_FIELD = 'email' 

	def __str__(self):
		return self.email



class GuestContactUs(models.Model):
	full_name= models.CharField(max_length= 40)
	email= models.EmailField(unique=False)
	question= models.TextField()

class Blogs(models.Model):
	TOPICS=(
		('1','Stress'),
		('2','Depression'),            
		('3','Anxiety'),
		('4','OCD'),
		('5','Eating Disorders'),
		('6','Relationships'),
		('7','Work Stress'),
		('8','Self Doubt'),
		('9','Addiction and Substance Abuse'),
		('10','Suicidal Tendency'),
		)
	
	

	therapist_id= models.ForeignKey(User, on_delete=models.CASCADE)
	topic= models.CharField(max_length=20, choices=TOPICS, blank=False, null=False )
	title= models.CharField(unique= True, max_length= 30)
	subtitle= models.CharField(unique= True, max_length= 75)
	date= models.DateField(auto_now_add=True)
	content= models.TextField(unique=True)
	favourited_by = models.ManyToManyField(User, related_name="favourited_blogs")
	



























# Create your models here.)
# class Patient(models.Model):
# 	GENDER=[
# 	('1','M'),
# 	('2','F'),
# 	('3','transgender'),
# 	('4',"don't want to specify"),
# 	]
# 	id= models.AutoField(primary_key=True)
# 	email= models.EmailField(unique=True)
# 	f_name= models.CharField(max_length=20)
# 	l_name= models.CharField(max_length=20)
# 	gender= models.CharField(max_length=20, choices=GENDER, default="2")
# 	age= models.IntegerField()
# 	phone= models.CharField(max_length=11, unique=True)

	# def __str__(self):
	# 	return self.gender
# many to many
# class Bread(models.Model):
# 	breadtype= models.CharField(max_length=20)

# class Topping(models.Model):
# 	name=models.CharField(max_length=20)
# 	quantity=models.IntegerField()
	

# class Pizza(models.Model):
# 	name=models.CharField(max_length=20)
# 	toppings=models.ManyToManyField(Topping)
# 	bread=models.ManyToManyField(Bread)
# #many to one
# class Singer(models.Model):
# 	name=models.CharField(max_length=20, unique=True)
# 	def __str__(self):
# 		return self.name

# class Song(models.Model):
# 	singername= models.ForeignKey(Singer, to_field="name", on_delete= models.CASCADE)
# 	name=models.CharField(max_length=20)
# 	lyrics=models.TextField()

# #onetoone
# class Person(models.Model):
# 	name=models.CharField(max_length=20)


# class Passport(models.Model):
# 	passportno=models.CharField(unique=True, max_length=10)
# 	f_personid=models.OneToOneField(Person, on_delete=models.CASCADE)


