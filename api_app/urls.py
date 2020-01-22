from django.urls import path
from . import views

urlpatterns = [
    path('analyze/', views.api_req, name='api'),
    path('analyze', views.api_req, name='api'),
    path('', views.index, name='index'),
]
