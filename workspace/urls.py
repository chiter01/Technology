from django.urls import path
from . import views


urlpatterns = [
    path('create_pradact/', views.create_pradact, name='create_pradact'),
    path('delete/<int:id>/', views.delete_pradact, name='delete_pradact'),
    path('ubdate/<int:id>/', views.ubdate_pradact, name='ubdate_pradact'),
    path('login/', views.login_profile, name='login'),
    path('logout/', views.logout_profile, name='logout'),
    path('register/', views.register, name='register'),
    path('', views.workspace, name='workspace'),
]