from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    data = request.POST.get('data', '')
    print(data)
