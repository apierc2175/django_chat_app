from django.urls import path
from . import views

app_name = 'chats'

urlpatterns = [
    path("", views.index, name='index'),
    path('add/', views.CreateView.as_view(), name='create'),
    path('<int:pk>/comment/new/', views.ChatDetailView.as_view(), name='comment'),
    # path('<int:pk>/comment/add/', views.CommentCreateView.as_view(), name='comment-add'),
    path('<int:pk>/', views.ChatDetailView.as_view(), name='chat_detail'),
]
