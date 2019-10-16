from django.urls import path
from . import views

app_name = 'accounts'
# changed url from profile-create to profile
urlpatterns = [
    path('login/', views.LoginView.as_view(), name="login"),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('profile-detail/', views.ProfileDetailView.as_view(), name='profile-detail'),
    path('profile/', views.ProfileCreateView.as_view(), name='profile-create'),
]
