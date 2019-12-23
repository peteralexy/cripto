from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def page(request):
    return render(request, 'page.html')