from django.shortcuts import render, HttpResponseRedirect, reverse, HttpResponse
from .models import Good
from .forms import AddForm
from django.core import serializers


def index(request):
    goods = Good.objects.all()
    if request.method == 'POST':
        form = AddForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('index'))
    else:
        form = AddForm()
    context = {'goods': goods,
               'form': form}
    return render(request, 'index.html', context=context)


def add_good(request):
    if request.method == 'POST':
        form = AddForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('index'))
    else:
        form = AddForm()
    context = {'form': form}

    return render(request, 'add_good.html', context)


def ajax_handler(request):
    goods = Good.objects.all()
    data = serializers.serialize('json',goods)
    return HttpResponse(data, content_type='text/html')

