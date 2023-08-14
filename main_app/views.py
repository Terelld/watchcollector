from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView

from .models import Watch, Accessory
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
    id_list = watch.accessorys.all().values_list('id')
    accessorys_watch_doesnt_have = Accessory.objects.exclude(id__in=id_list)                                            
    service_form = ServiceForm()
    return render(request, 'watches/detail.html', { 
        'watch' : watch, 'service_form': service_form,
        'accessorys' : accessorys_watch_doesnt_have
    })

def add_service(request, watch_id):
    form = ServiceForm(request.POST)
    if form.is_valid():
        new_service = form.save(commit=False)
        new_service.watch_id = watch_id
        new_service.save()
    return redirect('detail', watch_id=watch_id)

class WatchCreate(CreateView):
    model = Watch
    fields = ['brand', 'model', 'color', 'band_material', 'interface', 'description']

class WatchUpdate(UpdateView):
    model= Watch
    fields = '__all__'
    

class WatchDelete(DeleteView):
    model = Watch
    success_url = '/watches'



class AccessoryList(ListView):
  model = Accessory

class AccessoryDetail(DetailView):
  model = Accessory

class AccessoryCreate(CreateView):
  model = Accessory
  fields = '__all__'

class AccessoryUpdate(UpdateView):
  model = Accessory
  fields = ['name', 'color']

class AccessoryDelete(DeleteView):
  model = Accessory
  success_url = '/accessorys'

def assoc_accessory(request, watch_id, accessory_id):
  Watch.objects.get(id=watch_id).accessorys.add(accessory_id)
  return redirect('detail', watch_id=watch_id)


def unassoc_accessory(request, watch_id, accessory_id):
  Watch.objects.get(id=watch_id).accessorys.remove(accessory_id)
  return redirect('detail', watch_id=watch_id)
