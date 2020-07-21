from .models import Todo
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class todoForm(ModelForm):
    class Meta:
        model = Todo
        fields = '__all__'



class signupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(signupForm, self).save(commit=False)
        user.email = self.cleaned_data["email","username"]
        if commit:
            user.save()
        return user
        