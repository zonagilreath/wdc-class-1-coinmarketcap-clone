from django.shortcuts import render

from cryptocoins.models import Cryptocurrency

def index(request):
    coins = Cryptocurrency.objects.all().order_by('rank')
    return render(request, 'index.html', {
        'coins': coins
    })
