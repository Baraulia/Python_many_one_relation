from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include

from .views import Book_View

urlpatterns = [
    path('', Book_View, name='book_name'),


]