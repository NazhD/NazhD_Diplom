from django.shortcuts import render, redirect, get_object_or_404
from .models import ImageFile, VideoFile
from profiles.models import UserPage


def index(request):
    return render(request, 'warhammer/index.html')


def load_images(request):
    baza = ImageFile.objects.all()
    return render(request, 'warhammer/load-images.html', {"img": baza})


def image_img(request, image_id):
    image = get_object_or_404(ImageFile, pk=image_id)
    return render(request, 'warhammer/image_img.html',{"image": image})


def load_video(request):
    video_list = VideoFile.objects.all
    return render(request, 'warhammer/load-video.html', {'video_list': video_list})


def video_play(request, video_id):
    vid = get_object_or_404(VideoFile, pk=video_id)
    return render(request, 'warhammer/video-play.html',{"vid": vid})