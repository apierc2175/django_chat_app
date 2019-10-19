from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views import generic
from django.views.generic.edit import CreateView
#reverse lazy allows it to fully complete before executing
from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView
from .models import CustomUser, Profile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from .forms import CustomUserCreationForm

User = get_user_model()
# Create your views here.

class SignUpView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('accounts:login')
    template_name = 'registration/signup.html'

class LoginView(generic.CreateView):
    form_class = UserCreationForm
    template_name = 'login.html'
    success_url = reverse_lazy('index')

class ProfileCreateView(generic.CreateView):
    model = Profile
    template_name = 'registration/profile_create.html'
    success_url = reverse_lazy('chats:index')
    # success_url = reverse_lazy('accounts:profile-detail')
    fields = ('bio', 'location', 'avatar',)

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

def profile_detail(request):
    profile_list = Profile.objects.all()

    context = {
        'profile_list': profile_list,
    }

    return render(request, 'registration/profile_detail.html', context)

class ProfileDetailView(generic.DetailView):
    model = Profile
    template_name = 'registration/profile_detail.html'

    def get_object(self):
        return get_object_or_404(User, pk=self.request.user.id)


class UserCommentDetailView(generic.DetailView):
    model = User
    template_name = 'user_comment.html'

    def get_object(self):
        return get_object_or_404(User, pk=self.request.user.id)
