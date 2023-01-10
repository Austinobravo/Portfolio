from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(About_me)
class About_meAdmin(admin.ModelAdmin):
    list_display = ['name', 'email']

@admin.register(Projects)
class ProjectsAdmin(admin.ModelAdmin):
    list_display = ['title', 'link']

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email']