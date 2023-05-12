from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms
# from users.models import User
from django.utils.translation import gettext_lazy as _


#
User = get_user_model()

class UserCreationForm(UserCreationForm):
    email = forms.EmailField(
        label=_("Email"),
        max_length=254,
        widget=forms.EmailInput(attrs={"autocomplete": "email"}),
    )
    # username = forms.CharField(label = 'username',widget = forms.TextInput(attrs = {'class': 'form-input'}))
    # password1 = forms.CharField(label = 'password1',widget = forms.TextInput(attrs = {'class': 'form-input'}))
    # password2 = forms.CharField(label = 'password2',widget = forms.TextInput(attrs = {'class': 'form-input'}))
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username','id','first_name','last_name')

class RangeForm(forms.Form):
    min_value = forms.IntegerField(label='min')
    max_value = forms.IntegerField(label='max')