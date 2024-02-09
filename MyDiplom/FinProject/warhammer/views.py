from django.shortcuts import render
from .models import ImageFile


menu = [
    {"title": "Главная"},
    {"title": "Регистрация"},
    {"title": "Вход"},
]

baza = ImageFile.objects.all()


def index(request):
    return render(request, 'warhammer/index.html', {"menu": menu})


def load_images(request):
    return render(request, 'warhammer/load-images.html', {"img": baza, "menu": menu})




