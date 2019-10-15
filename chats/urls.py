from django.urls import path
from . import views

app_name = 'chats'

urlpatterns = [
    path("", views.index, name='index'),
    path('add/', views.CreateView.as_view(), name='create'),
]
