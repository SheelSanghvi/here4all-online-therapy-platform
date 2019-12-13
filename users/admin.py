from django.contrib import admin
from .models import *

# Register your models here.
class GuestContactUsAdmin(admin.ModelAdmin):
	list_display= ['full_name', 'email', 'question']

class BlogsAdmin(admin.ModelAdmin):
	list_display= [ 'id', 'therapist_id', 'topic', 'title', 'subtitle', 'date', 'content']

class UserAdmin(admin.ModelAdmin):
	list_display= ['id', 'user_type','email', 'f_name', 'l_name', 'gender']

admin.site.register(User, UserAdmin)
admin.site.register(GuestContactUs, GuestContactUsAdmin)
admin.site.register(Blogs,BlogsAdmin)
# class ProfileAdmin(admin.ModelAdmin):
# 	list_display= ['id']

# admin.site.register(Profile, ProfileAdmin)

























# class PatientAdmin(admin.ModelAdmin):
# 	# fields = ('email', 'f_name', 'l_name', 'gender', 'age','phone')
# 	list_display = ('email','f_name', 'l_name', 'gender', 'age','phone')

# admin.site.register(Patient, PatientAdmin)
#manytomany
# class PizzaAdmin(admin.ModelAdmin):
# 	list_display=('name','id')
	# def get_products(self, obj):
 #        return "\n".join([p.products for p in obj.product.all()])

# admin.site.register(Topping)
# admin.site.register(Pizza,PizzaAdmin)
# admin.site.register(Bread)

#manytoone
# class SingerAdmin(admin.ModelAdmin):
# 	list_display=('id','name')
# class SongAdmin(admin.ModelAdmin):
# 	list_display=('id','name', 'singername')


# admin.site.register(Singer,SingerAdmin)
# admin.site.register(Song,SongAdmin)

#onetoone
# class PersonAdmin(admin.ModelAdmin):
# 	list_display=('id','name')

# class PassportAdmin(admin.ModelAdmin):
# 	list_display=('id','passportno','f_personid')

# admin.site.register(Person,PersonAdmin)
# admin.site.register(Passport, PassportAdmin)



