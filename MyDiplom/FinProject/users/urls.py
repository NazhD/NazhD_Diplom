from django.urls import path
from . import views


urlpatterns = [
    path('reg/', views.registration, name="registration"),
    path('login/', views.login_user, name="login_user"),
    path('logout/', views.logout_user, name="logout_user"),
    path('page/', views.page_user, name="page_user"),
    path('page/<str:pk>/', views.user_blog, name="user_blog"),

]