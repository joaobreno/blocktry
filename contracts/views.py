from django.shortcuts import render
from .models import Contract



def index(request):
    return render(request, 'index.html')

def contracts(request):
    contracts = Contract.objects.order_by('name')
    data = {
        'contracts': contracts
        }
    return render(request, 'team.html', data)

def post(request):
    return render(request, 'post.html')

def contact(request):
    return render(request, 'contact.html')

# Create your views here.
