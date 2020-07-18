from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path("hello", views.hello  ),
    path("comment", views.comment ),
    path("post", views.post ),
]