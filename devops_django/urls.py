from django.contrib import admin
from django.http import HttpRequest, HttpResponse
from django.urls import path
from django.shortcuts import render


def hello(request: HttpRequest) -> HttpResponse:
    return render(request, 'index.html')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', hello),
]
