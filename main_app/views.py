from django.shortcuts import render
from .models import Watch


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
    return render(request, 'watches/detail.html', { 'watch' : watch })