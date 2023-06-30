from django.contrib import admin

from library.models import Author, Category, Publisher

admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Publisher)
