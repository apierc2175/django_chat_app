from django.urls import path
from . import views

app_name = 'chats'

urlpatterns = [
    path("", views.index, name='index'),
    path('add/', views.CreateView.as_view(), name='create'),
    # path('<int:pk>/comment/new/', views.ChatDetailView.as_view(), name='comment'),
    path('<int:pk>/comment/new/', views.CommentCreateView.as_view(), name='add_comment'),
    path('<int:pk>/', views.TopicDetailView.as_view(), name='topic_detail'),
]
