from django.urls import path
from . import views


urlpatterns = [  
    path('<int:id>/', views.detail_pradact, name='detail_pradact'),
    path('', views.main, name='main'),
]