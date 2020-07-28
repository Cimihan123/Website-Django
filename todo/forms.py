from .models import *
from django.forms import ModelForm,Form
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms




class todoForm(ModelForm):
    class Meta:
        model = Todo
        fields = '__all__'
        


class commenForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={"placeholder" : "name"}),max_length='20')    
    comment = forms.CharField(label='comment',widget=forms.Textarea(attrs={"placeholder" : "comment"}))
    class Meta:
        model = Comment
        fields = ('name','comment')
        




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
        

