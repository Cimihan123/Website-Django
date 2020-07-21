from django.shortcuts import render,redirect
from .models import *
from .forms import *
from django.db.models import Q 
from django.views.generic import TemplateView, ListView
from django.contrib.auth import login, authenticate , logout
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.

def signup(request):
    template_name = 'signup.html'
    form = signupForm()
    if request.method == 'POST':
        form = signupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1','password2')
    
            user = authenticate(username=username,password=password)
            login(request, user)
            return redirect('login')
            messages.info(request, 'Username OR password is incorrect')
        else:
            form = signupForm()
    context = {

        'form' : form
    }

    return render(request,template_name,context)


def login_user(request):
    template_name = 'login.html'
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request,user)
                return redirect('index')
                

            else:
                return HttpResponse("Your account was inactive.")
                
        else:
            messages.info(request, 'Username OR password is incorrect')


    context ={

    }
    return render(request,template_name,context)



def logoutUser(request):
    logout(request)

    return redirect('login')


@login_required(login_url='login')
def todo(request):

    template_name = 'todo.html'
    title = Todo.objects.all()

    form = todoForm()

    if request.method == 'POST':
        form = todoForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('index')


    context = {

        'todo' : title,
    }

    return render(request,template_name,context)



@login_required(login_url='login')
def update(request,pk):

    template_name = 'update.html'
    title = Todo.objects.get(id=pk)

    form = todoForm(instance=title)

    if request.method == 'POST':
        form = todoForm(request.POST,instance=title)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {

        'todo' : title,
    }



    
    return render(request,template_name,context)



@login_required(login_url='login')
def delete(request,pk):
    template_name = 'delete.html'
    title = Todo.objects.all()
    title = Todo.objects.get(id=pk)
    if request.method =="POST": 
    
        title.delete()
        return redirect('index')

    context = {

        'todo' : title,
    }

    return render(request,template_name,context)



class SearchResultsView(ListView):
    model = Todo
    template_name = 'search_results.html'
    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Todo.objects.filter(
        Q(title__icontains=query) | Q(decription__icontains=query)
        )
        return object_list