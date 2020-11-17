from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model

from accounts.forms import UCreateForm, UChangeForm
from accounts.models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = UCreateForm
    form = UCreateForm
    model = CustomUser
    list_display = ['email', 'username']


admin.site.register(CustomUser, CustomUserAdmin)
