from django.shortcuts import render, get_object_or_404

from cryptocoins.models import Cryptocurrency

def index(request):
    coins = Cryptocurrency.objects.all().order_by('rank')

    if 'order_by' in request.GET:
        field = request.GET['order_by']
        if field in dir(Cryptocurrency):
            order_type = request.GET.get('order_type', 'asc')
            if order_type == 'desc':
                field = '-{}'.format(field)
            coins = coins.order_by(field)

    if 'min_price' in request.GET:
        try:
            min_value = int(request.GET['min_price'])
        except ValueError:
            pass
        else:
            coins = coins.filter(price_usd__gte=min_value)

    return render(request, 'index.html', {
        'coins': coins
    })


def detail(request, coin_id):
    coin = get_object_or_404(Cryptocurrency, id=coin_id)
    return render(request, 'detail.html', {
        'coin': coin
    })
