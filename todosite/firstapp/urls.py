from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'firstapp'
urlpatterns = [
    path('register/', views.RegisterUser, name="register"),
	path('login/', views.LoginUser, name="login"),  
	path('logout/', views.LogoutUser, name="logout"),
    path('', views.Home, name="home"),
    path('task/', views.ToDo, name='task'),
    path('update_task/<str:pk>/', views.updateTask, name="update_task"),
    path('delete_task/<str:pk>/', views.deleteTask, name="delete_task"),
    path('status/', views.status, name="status"),
    path('delete_all/', views.deleteAll, name="delete_all"),
    path('about/', views.aboutUs, name="about"),
    path('notes/<str:pk>/', views.Note, name="note"),
    path('priority/', views.priority, name="priority"),
]