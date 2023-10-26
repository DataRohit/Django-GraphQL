from django.contrib import admin
from users.models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ("email", "username", "is_staff", "is_active", "is_superuser")
    list_filter = ("is_staff", "is_active", "is_superuser")
    search_fields = ("email", "username")
    ordering = ("email",)


# Register your models here.
admin.site.register(User, UserAdmin)
