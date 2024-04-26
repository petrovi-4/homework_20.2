from django.shortcuts import render

from catalog.models import Product


def index(request):
    context = {
        'title': 'Главная',
        'products': Product.objects.all().order_by('-id')[:5]

    }
    print(context['products'])
    return render(request, 'catalog/index.html', context=context)


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(f'Новое сообщение от пользователя {name}({email}): {message}')
    context = {
        'title': 'Контакты'
    }
    return render(request, 'catalog/contacts.html', context)


def get_product(request, pk):
    product = Product.objects.get(pk=pk)
    context = {
        'title': product.product_name,
        'product': product
    }
    print(context['product'])
    return render(request, f'catalog/product.html', context=context)
