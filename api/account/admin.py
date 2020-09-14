from django.contrib import admin
from .models import User
# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_dispay = ['username', 'email', 'phone_number']
    list_dispay_link = ['username', 'email', 'phone_number']