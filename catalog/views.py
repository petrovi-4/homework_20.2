from django.shortcuts import render

from catalog.models import Product


def index(request):
    context = {
        'title': 'skystore',
        'products': Product.objects.all().order_by('-id')[:5]
    }
    print(context['products'])
    return render(request, 'catalog/home.html', context=context)


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(f'Новое сообщение от пользователя {name}({email}): {message}')
    return render(request, 'catalog/contacts.html')
