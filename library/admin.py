from django.contrib import admin

from library.models import Author, Book, Category, Publisher

admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Category)
admin.site.register(Publisher)
