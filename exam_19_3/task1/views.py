from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import *
from .models import *



def get_all_buyers():
    return Buyer.objects.all()

def get_all_games():
    return Game.objects.all()


def main(request):
    page_name = 'Главная страница'
    menu = ['Главная', 'Игры', 'Корзина']
    context = {
        'page_name': page_name,
        'menu': menu,
    }
    return render(request, 'menu.html', context)


def second_page(requests):
    page_name = 'Игры'
    menu = ['Главная', 'Игры', 'Корзина']
    content = get_all_games()
    context = {
        'page_name': page_name,
        'menu': menu,
        'content': content,
    }
    return render(requests, 'second_page.html', context)


def third_page(requests):
    page_name = 'Корзина'
    menu = ['Главная', 'Игры', 'Корзина']
    basket = []
    len_bas = len(basket)
    content = 'Кажется здесь пусто :)'
    context = {
        'page_name': page_name,
        'menu': menu,
        'basket': basket,
        'content': content,
        'len_bas': len_bas,
    }
    return render(requests, 'third_page.html', context)




def sign_up_by_django(request):
    info = {}

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']
            all_buyers = get_all_buyers()
            if password != repeat_password:
                info['error'] = "Пароли не совпадают."
            elif age < 18:
                info['error'] = "Возраст должен быть не менее 18 лет."
            elif any(buyer.name == username for buyer in all_buyers):
                info['error'] = "Логин уже занят."
            else:
                Buyer.objects.create(name=username, balance=100.00, age=age)
                return HttpResponse(f"Приветствуем, {username}!")
    else:
        form = UserRegisterForm()
    info['form'] = form
    return render(request, 'registration_page.html', info)


def get_all(request):
    a = Buyer.objects.all()
    b = Game.objects.all()
    context = {
        'buyers': a,
        'games': b,
    }
    return render(request, 'test.html', context)

