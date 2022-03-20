from django.shortcuts import render

# Create your views here.
from .models import BookModel, AuthorModel


def Book_View(request):
    books = BookModel.objects.all()

    return render(request, 'index.html', {'books': books})
