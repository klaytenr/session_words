from django.conf.urls import url 
from . import views

urlpatterns = [
    url(r'^session_word$', views.index),
    url(r'session_word/add_new', views.add_new),
    url(r'sesion_word/reset', views.reset)
]