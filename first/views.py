from django.http import HttpResponse
from django.shortcuts import render
from first.models import Book

def add(request):
    Book.objects.create(name="红楼梦",price=99)
    return HttpResponse("添加完成")