import json

from django.http import HttpResponse
from django.shortcuts import render
from first.models import Book, Catalog


def allCatas(req):
    catas = Catalog.objects.all()
    x=json.dumps(catas)
    return HttpResponse(x)