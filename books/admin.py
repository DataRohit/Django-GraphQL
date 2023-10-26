from django.contrib import admin

from books.models import *
from books.admin import *


class BooksAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "category")
    search_fields = ("title", "author", "category")
    list_filter = ["category"]


admin.site.register(Books, BooksAdmin)
