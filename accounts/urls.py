from django.urls import path
from . import views

app_name = 'accounts'
# changed url from profile-create to profile
urlpatterns = [
    path('login/', views.LoginView.as_view(), name="login"),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    # path('<int:pk>/profile-detail/', views.ProfileDetailView.as_view(), name='profile-detail'),
    path('profile-detail/', views.profile_detail, name='profile-detail'),
    path('profile/', views.ProfileCreateView.as_view(), name='profile-create'),
    path('user/comments/', views.UserCommentDetailView.as_view(), name='user_comment_list')
]
