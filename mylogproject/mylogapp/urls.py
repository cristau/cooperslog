from django.urls import path
from . import views

urlpatterns = [
    path('', views.log_page, name='log_page'),
    path('submit_activity/success/', views.success, name='success')
]
