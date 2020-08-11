
from django.urls import path
from . import views
from .views import  SearchResultsView
from django.contrib.auth import views as auth_views



urlpatterns = [
 
    path('', views.index,name='index'),    
    path('tag/<str:tags>/', views.tagChoice,name='tag'),    
    path('detail/<str:pk>', views.detailView,name='detail'),
    path('search/', SearchResultsView.as_view(), name='search_results'),
    
    #CRUD

    path('cpost/', views.createPOST,name='cpost'),
    path('update/<str:pk>', views.update,name='update'),
    path('delete/<str:pk>', views.delete,name='delete'),

  

]


