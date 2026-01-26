from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import StudentProfile
# Register your models here.
class StudentProfileInline(admin.StackedInline):
    model = StudentProfile
    can_delete = False
    extra = 0
    max_num = 1

class UserAdmin(BaseUserAdmin):
    inlines = [StudentProfileInline]

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
