from django.urls import path
from . import views


urlpatterns = [
    path('', views.process_monitor, name='process_monitor'),

]