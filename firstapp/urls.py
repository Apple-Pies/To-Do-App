from django.urls import path
from . import views

app_name = 'firstapp'
urlpatterns = [
    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),  
    path('logout/', views.logoutUser, name="logout"),
    path('', views.home, name="home"),
    path('task/', views.task, name="task"),
    path('update_task/<str:pk>/', views.updateTask, name="update_task"),
    path('delete_task/<str:pk>/', views.deleteTask, name="delete_task"),
    path('status/', views.status, name="status"),
    path('delete_all/', views.delete_all, name="delete_all"),

    path('about/', views.aboutUs, name="about"),
    path('notes/<str:pk>/', views.Note, name="note"),
    path('priority/', views.priority, name="priority"),

    
]