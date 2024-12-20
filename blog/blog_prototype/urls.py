from django.contrib.auth import views
from django.urls import path

from blog_prototype.views import blog as blog_views
from blog_prototype.views import user as user_views

urlpatterns = [
    path('', blog_views.post_list, name='post-list'),
    path('create/', blog_views.post_create, name='post-create'),
    path('view/<int:post_id>', blog_views.post_view, name='post-view'),

    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('register/', user_views.register, name='register')
]
