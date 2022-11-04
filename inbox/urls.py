from django.urls import path

from . import views

urlpatterns = [
    path('direct_message', views.direct_message, name='direct_message')
]