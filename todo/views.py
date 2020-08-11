from django.shortcuts import render,redirect
from .models import *
from .forms import *
from django.db.models import Q 
from django.views.generic import TemplateView, ListView
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
import requests
from isodate import parse_duration
from django.conf import settings
from .filters import *

# Create your views here.


def index(request):

    template_name = 'index.html'
    title = Todo.objects.all()

    filter_post = SearchFilter(request.GET,queryset=title)
    title = filter_post.qs


  
    paginator = Paginator(title, 6)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)


    form = todoForm()

    if request.method == 'POST':
        form = todoForm(request.POST)
        if form.is_valid():
            form.save()

    context = {

        'todo' : page_obj,
        'filter_post' : filter_post
       
    }

    return render(request,template_name,context)



def tagChoice(request,tags):

    template_name = 'tags.html'

    tag = Todo.objects.filter(tags=tags)

    context = {
        'todo' : tag


    }



    return render(request,template_name,context)





@login_required(login_url='index')
def createPOST(request):

    template_name = 'postCreate.htm'
    form = PostForm(request.POST,request.FILES)

    if request.method == 'POST':
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
             form.save()
        return redirect('index')

    context = {

        'form' : form
    }

    return render(request,template_name,context)

    



 
def update(request,pk):

    template_name = 'update.html'

    title = Todo.objects.get(id=pk)
    form = todoForm(instance=title)

    if request.method == 'POST':
        form = todoForm(request.POST,request.FILES,instance=title)
        if form.is_valid():
            form.save()
            return redirect('index')
           

    context = {

        'todo' : title,
        'form' : form,
    }



    
    return render(request,template_name,context)
 
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


