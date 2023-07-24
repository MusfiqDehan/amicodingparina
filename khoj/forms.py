from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


def validate_comma_separated_integer_list(value):
    values = value.split(',')
    for val in values:
        try:
            int(val)
        except ValueError:
            # raise exception if value is not an integer
            raise forms.ValidationError(f"{val} is not an integer")


class InputForm(forms.Form):
    input_values = forms.CharField(
        validators=[validate_comma_separated_integer_list])
    search_value = forms.IntegerField()
