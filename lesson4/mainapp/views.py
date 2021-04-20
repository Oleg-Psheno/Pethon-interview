from django.shortcuts import render
from .models import Good

def index(request):
    goods = Good.objects.all()
    context = {'goods':goods}
    return render(request,'index.html', context=context)