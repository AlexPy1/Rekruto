from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse(f"<h1>Hello {request.GET['name']}! {request.GET['message']}</h1>")
# Create your views here.
