from django.shortcuts import render

watches = [
    {'brand': 'Fossil', 'model':'', 'band material': 'metal', 'color': 'gun metal', 'interface': 'digital', 'description': 'casual'},
    {'brand': 'Rolex', 'model':'', 'band material': 'leather', 'color': 'brown', 'interface': 'analog', 'description': 'formal'},
    {'brand': 'Nike', 'model':'', 'band material': 'silicone', 'color': 'black', 'interface': 'digital', 'description': 'athletic'},
]

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def watches_index(request):
    return render(request, 'watches/index.html')