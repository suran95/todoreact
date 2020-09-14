from django.contrib import admin
from .models import Students
from .models import Scores
# Register your models here.
@admin.register(Students)
class UserAdmin(admin.ModelAdmin):
    list_dispay = ['username', 'email', 'phone_number']

@admin.register(Scores)
class UserAdmin(admin.ModelAdmin):
    list_dispay = ['name']
    