from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path("home/", views.home, name="home"),
    path("contact/", views.guestContactUs, name="contact"),
    path("whytherapy/", views.whytherapy, name="whytherapy"),
    path("ourteam/", views.ourteam, name="ourteam"),
    path("register/",views.register, name="register"),
    path("login/",auth_views.LoginView.as_view(template_name='users/login.html'), name="login"),
    path("logout/",auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('dashboard/', views.dashboard, name= 'dashboard'),
    path('dashboard/blogs', views.therapistDashboardBlogs, name= 'therapistDashboardBlogs'),
    # path('dashboard/profilet', views.therapistDashboardProfile, name= 'therapistDashboardProfile'),
    # path('dashboard/profilep', views.patientDashboardProfile, name= 'patientDashboardProfile'),
    path('blogs/', views.blogs, name='blogs'),
    path('blogs/<str:url_topic>', views.topicBlogs, name='topicBlogs'),




    #rest framework urls
    path('blogs_api/', views.BlogsAPIView.as_view(), name='blogs-api'),
    path('blogs_rud/<int:id>/', views.BlogsRudView.as_view(), name='blogs-rud'),

    path('guestContactUs_api/', views.GuestContactUsAPIView.as_view(), name='guestContactUs-api'),
    path('guestContactUs_rud/<str:email>', views.GuestContactUsRudView.as_view(), name='guestContactUs-rud'),

    path('user_api/', views.UserAPIView.as_view(), name='user-api'),
    path('user_rud/<int:id>/', views.UserRudView.as_view(), name='buser-rud'),

    path('favourite_api/<int:id>', views.FavouriteBlogView.as_view(), name='favourite-api'),


]


