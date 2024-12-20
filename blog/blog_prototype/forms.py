from django import forms
from django.contrib.auth.forms import UserCreationForm

from blog_prototype.models.user import User


class SignUpForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', )
