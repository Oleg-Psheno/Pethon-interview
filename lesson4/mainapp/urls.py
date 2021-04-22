
from django.urls import path, include
from .views import index,add_good, ajax_handler

urlpatterns = [

    path('',index, name='index'),
    path('new', add_good, name = 'new_good'),
    path('ajax_handler', ajax_handler, name = 'ajax_handler')
]
