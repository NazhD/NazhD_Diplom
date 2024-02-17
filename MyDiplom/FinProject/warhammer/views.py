from django.shortcuts import render, redirect, get_object_or_404
from .models import ImageFile, VideoFile


menu = [
    {"title": "Главная"},
    {"title": "Регистрация"},
    {"title": "Вход"},
]

baza = ImageFile.objects.all()
video_list = VideoFile.objects.all


def index(request):
    return render(request, 'warhammer/index.html', {"menu": menu})


def load_images(request):
    return render(request, 'warhammer/load-images.html', {"img": baza, "menu": menu})


def load_video(request):
    return render(request, 'warhammer/load-video.html', {'video_list': video_list})


def video_play(request, video_id):
    vid = get_object_or_404(VideoFile, pk=video_id)
    return render(request, 'warhammer/video-play.html',{"vid": vid})