from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as ExtendUserAdmin
from django.contrib.auth.models import User
from . models import UserProfile


class UserProfileAdmin(admin.StackedInline):
    model = UserProfile


class UserAdmin(ExtendUserAdmin):
    inlines = (UserProfileAdmin,)


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
