
from django.urls import path
from . import views
from .views import  SearchResultsView
from django.contrib.auth import views as auth_views



urlpatterns = [
    path('', views.todo,name='index'),
    path('update/<str:pk>', views.update,name='update'),
    path('delete/<str:pk>', views.delete,name='delete'),
    path('detail/<str:pk>', views.detailView,name='detail'),
    path('search/', SearchResultsView.as_view(), name='search_results'),
    path('signup/',views.signup,name='signup'),
    path('login/',views.login_user,name='login'),
    path('logout/',views.logoutUser,name='logout'),
    path('reset_password/',auth_views.PasswordResetView.as_view(template_name='password_reset.html'),name='reset_password'),
    path('reset_password_sent/',auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path('reset_password_complete/',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),
  

]


