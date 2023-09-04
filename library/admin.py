from django.contrib import admin

from library.models import Author, Book, Category, Publisher, Shopping

admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Category)
admin.site.register(Publisher)
admin.site.register(Shopping)
