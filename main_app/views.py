from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Watch
from .forms import ServiceForm


# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def watches_index(request):
    watches = Watch.objects.all()
    return render(request, 'watches/index.html', {
        'watches': watches 
    })

def watches_detail(request, watch_id):
    watch = Watch.objects.get(id=watch_id)
    service_form = ServiceForm()
    return render(request, 'watches/detail.html', { 
        'watch' : watch, 'service_form': service_form 
    })


class WatchCreate(CreateView):
    model = Watch
    fields = '__all__'

class WatchUpdate(UpdateView):
    model= Watch
    fields = '__all__'
    

class WatchDelete(DeleteView):
    model = Watch
    success_url = '/watches'
