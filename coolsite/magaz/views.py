from django.http import HttpResponse
from django.shortcuts import render

menu=["Главная страница","О нас","Категории","Отзывы"]
def index(request):
    return render(request, 'magaz/index.html',{'menu':menu,'title':'Главная страница'})

def information(request):
    return render(request, 'magaz/info.html',{'menu':menu,'title':'О нас'})

