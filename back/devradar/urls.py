from django.urls import path
from devradar import views

urlpatterns = [
    path('devs/', views.dev_list),
    path('devs/<int:pk>/', views.dev_detail),
]