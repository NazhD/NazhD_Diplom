from django.shortcuts import render, get_object_or_404
from .models import UserPage
from warhammer.models import *
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist


def page_user(request):
    search_query = ""
    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')
    users_name = UserPage.objects.filter(title__icontains=search_query)
    context = {"users_name": users_name,
               "search_query": search_query, }

    return render(request, 'profiles/page.html', context)


def user_blog(request, pk):
    users_blog = User.objects.get(id=pk)
    try:
        page = UserPage.objects.get(username_id=pk)
    except ObjectDoesNotExist:
        b = UserPage(username_id=pk)
        b.save()
        page = UserPage.objects.get(username_id=pk)
    context = {
        "users_blog": users_blog,
        "page": page,
    }
    if request.GET.get('btr') == "Картинки":
        baza = ImageFile.objects.all()
        c = {"baza": baza}
        context.update(c)

        print(baza[1].author.username)


    if request.GET.get('btr') == "Видео":
        video_list = VideoFile.objects.all()
        c = {"video_list": video_list}
        context.update(c)

    if request.method == request.FILES or request.POST:
        if 'file' in request.FILES:
            page.image = request.FILES['file']
            page.save()
        if "title" in request.POST:
            page.title = request.POST['title']
            page.save()

    return render(request, 'profiles/user_blog.html', context)
