from django.shortcuts import render,HttpResponseRedirect,reverse
from .models import Good
from .forms import AddForm

def index(request):
    goods = Good.objects.all()
    context = {'goods':goods}
    return render(request,'index.html', context=context)

def add_good(request):
    if request.method == 'POST':
        form = AddForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('index'))
    else:
        form = AddForm()
    context = {'form':form}

    return render(request,'add_good.html', context)
