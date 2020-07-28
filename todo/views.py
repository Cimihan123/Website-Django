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
from django.core.paginator import Paginator
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

  
    paginator = Paginator(title, 2)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)


    form = todoForm()

    if request.method == 'POST':
        form = todoForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('index')


    context = {

        'todo' : page_obj,
       
    }

    return render(request,template_name,context)



@login_required(login_url='login')
def update(request,pk):

    template_name = 'update.html'

    title = Todo.objects.get(pk=pk)
    form = todoForm()

    if request.method == 'POST':
        form = todoForm(request.POST,instance=title)
        if form.is_valid():
            form.save()
           

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





def detailView(request,pk):
    template_name = 'detail.html'
    detail = Todo.objects.get(pk=pk)
   
    comments = Comment.objects.filter(todo=detail)

    form = commenForm()
    if request.method == 'POST':
        form = commenForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.todo = detail
            comment.save()
            return redirect('detail', pk=detail.pk)
           
           
           
    context = {
      'detail' : detail,
      'form' : form,
      'comments' : comments


    }
    return render(request,template_name,context)


