
from django.urls import path, include
from .views import index,add_good

urlpatterns = [

    path('',index, name='index'),
    path('/new', add_good, name = 'new_good')
]
