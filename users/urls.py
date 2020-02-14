from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import *

urlpatterns = [
    path("home/", views.home, name="home"),
    path("contact/", views.guestContactUs, name="contact"),
    path("whytherapy/", views.whytherapy, name="whytherapy"),
    path("ourteam/", views.ourteam, name="ourteam"),
    path("register/",views.register, name="register"),
    path("login/",auth_views.LoginView.as_view(template_name='users/login.html'), name="login"),
    path("logout/",auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('', views.deleteAccount, name= 'deleteAccount'),
    path('dashboard/', views.dashboard, name= 'dashboard'),
    path('dashboard/blogs/', views.therapistDashboardBlogs, name= 'therapistDashboardBlogs'),
    path('dashboard/contact_patient/', views.therapistDashboardChat, name= 'therapistDashboardChat'),
    path('dashboard/contact_doctor/', views.patientDashboardChat, name= 'patientDashboardChat'),
    path('blogs/', views.blogs, name='blogs'),
    path('blogs/<str:url_topic>', views.topicBlogs, name='topicBlogs'),




    #rest framework urls
    path('blogs_api/', BlogsAPIView.as_view(), name='blogs-api'),
    path('blogs_rud/<int:id>/', BlogsRudView.as_view(), name='blogs-rud'),

    path('guestContactUs_api/', GuestContactUsAPIView.as_view(), name='guestContactUs-api'),
    path('guestContactUs_rud/<str:email>', GuestContactUsRudView.as_view(), name='guestContactUs-rud'),

    path('user_api/', UserAPIView.as_view(), name='user-api'),
    path('user_rud/<int:id>/', UserRudView.as_view(), name='buser-rud'),

    path('favourite_api/<int:id>', FavouriteBlogView.as_view(), name='favourite-api'),


]


