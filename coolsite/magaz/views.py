from django.http import HttpResponse
from django.shortcuts import render


from .models import *
menu=[{'title': "Главная страница", 'url_name': 'home'},
      {'title': "О нас", 'url_name': 'info'},
      {'title': "Категории", 'url_name': 'cat'},
      {'title': "Отзывы", 'url_name': 'feedback'}
      ]

def index(request):
    posts = Pants.objects.all()
    posts1 = Tshirt.objects.all()
    posts2 = Blouse.objects.all()
    context = {
        'posts': posts1,
        'posts1': posts2,
        'posts2': posts,
        'menu': menu,
        'title': 'Главная страница'
    }
    return render(request, 'magaz/index.html', context=context)

def information(request):
    return render(request, 'magaz/info.html',{'menu':menu,'title':'О нас'})
def categori(request):
    return HttpResponse("Категории")
def feedback(request):
    return HttpResponse("Отзывы")
def show_post(request,post_id):
    return HttpResponse(f"купить по id={post_id}")
