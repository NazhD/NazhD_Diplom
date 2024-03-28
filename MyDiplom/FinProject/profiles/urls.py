from . import views
from django.urls import path


urlpatterns = [
    path('page/', views.page_user, name="page_user"),
    path('page/<str:pk>/', views.user_blog, name="user_blog"),
]