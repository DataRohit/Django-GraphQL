from django.contrib import admin

from graphql_auth.models import *


class UserStatusAdmin(admin.ModelAdmin):
    list_display = ("user", "verified", "archived", "secondary_email")
    search_fields = ("user__username", "user__email", "secondary_email")
    list_filter = ("verified", "archived")


admin.site.register(UserStatus, UserStatusAdmin)
