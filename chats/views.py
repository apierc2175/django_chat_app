from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views import generic
from django.views.generic.edit import CreateView
#reverse lazy allows it to fully complete before executing
from django.urls import reverse_lazy, reverse
from django.views.generic.edit import DeleteView
from .models import Topic, Comment
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User

User = get_user_model()

def index(request):
    chat_list = Topic.objects.all()

    context = {
        'chat_list': chat_list,
    }

    return render(request, 'chats/index.html', context)

def your_comment(request):
    your_comment_list = comment_list = User.objects.filter()

    context = {
        'your_comment_list': your_comment_list,
    }

    return render(request, 'chats/your_comment.html', context)

def comment(request):
    comment_list = Comment.objects.all()

    context = {
        'comment_list': comment_list,
    }

    return render(request, 'chats/comment.html', context)

class CreateView(generic.CreateView):
    model = Topic
    fields = '__all__'
    template_name = 'chats/create.html'


class CommentCreateView(generic.CreateView):
    model = Comment
    fields = ('text',)
    template_name = 'chats/add_comment.html'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        form.instance.topic_id = self.kwargs['pk']
        return super(CommentCreateView, self).form_valid(form)


class TopicDetailView(generic.DetailView):
    model = Topic
    template_name = 'chats/topic_detail.html'

class ChatListView(generic.DetailView):
    model = Topic
    template_name = 'chats/comment.html'

    #on my chat maker make a model that is chatDetailView and inside have a def add_comment(self, pk)
