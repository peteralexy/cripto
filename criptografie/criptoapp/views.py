from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from .forms import VoteForm
import mysql.connector as mc

# Create your views here.
def index(request):
    return render(request, 'index.html')

def page(request):

    if request.method != 'POST':
        form = VoteForm()
    else:
        form = VoteForm(request.POST)
        if form.is_valid():
            #form.save()
            #open a connection to mysql workbench
            #mySQLconnection = mc.connect()

            return HttpResponseRedirect(reverse('criptoapp:index'))

    return render(request, 'page.html', {'form': form})