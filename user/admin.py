from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from user.models import User


class UserUserAdmin(UserAdmin):
    model = User

    #fieldsets = UserAdmin.fieldsets + (
            #(None, {'fields': ('some_extra_data',)}),
    #)

admin.site.register(User, UserUserAdmin)
