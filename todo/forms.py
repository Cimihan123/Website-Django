from .models import *
from django.forms import ModelForm,Form
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
        




class PostForm(ModelForm):
    class Meta:
        model = Todo
        fields =  '__all__'

        widgets = {


        
            'title' : forms.TextInput(attrs={'placeholder' : 'title'}),
            'decription' : forms.TextInput(attrs={'placeholder' : 'decription'}),
          
                
        }

        

        

