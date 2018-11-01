from django.shortcuts import render, get_object_or_404

from cryptocoins.models import Cryptocurrency

def index(request):
    coins = Cryptocurrency.objects.all().order_by('rank')
    return render(request, 'index.html', {
        'coins': coins
    })


def detail(request, coin_id):
    coin = get_object_or_404(Cryptocurrency, id=coin_id)
    return render(request, 'detail.html', {
        'coin': coin
    })
