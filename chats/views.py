from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views import generic
from django.views.generic.edit import CreateView
#reverse lazy allows it to fully complete before executing
from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView
from .models import Topic
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User

def index(request):
    chat_list = Topic.objects.all()

    context = {
        'chat_list': chat_list,
    }

    return render(request, 'chats/index.html', context)

class CreateView(generic.CreateView):
    model = Topic
    fields = '__all__'
    template_name = 'chats/create.html'

    #on my chat maker make a model that is chatDetailView and inside have a def add_comment(self, pk)
