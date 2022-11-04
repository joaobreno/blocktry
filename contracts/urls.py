from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contracts', views.contracts, name='contracts'),
    path('post', views.post, name='post'),
    path('contact', views.contact, name='contact')
]
