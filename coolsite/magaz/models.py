from django.db import models
from django.urls import reverse

# Create your models here.
Pants =[
    {'id':1, 'name': 'Джинсы', 'model': 'DECK', 'price': 5000},
    {'id':2, 'name': 'Спортивные штаны', 'model': 'spots', 'price': 4299},
    {'id':3, 'name': 'Шорты', 'model': 'chaos', 'price': 3599},
]

Tshirt =[
    {'id':1, 'name': 'футболка', 'model': 'DECK', 'price': 2000},
    {'id':2, 'name': 'футболка ', 'model': 'ПЫЩ', 'price': 1799},
    {'id':3, 'name': 'футболка', 'model': 'чиназес', 'price': 5000},
]

Blouse=[
    {'id':1, 'name': 'худи', 'model': 'DECK', 'price': 5000},
    {'id':2, 'name': 'зипка', 'model': 'stoneisland', 'price': 24299},
    {'id':3, 'name': 'худи', 'model': 'chaos', 'price': 6999},
]

class Pants(models.Model):
    name = models.CharField(max_length=30)
    model = models.CharField(max_length=30)
    price = models.IntegerField(blank=True)
    photo = models.ImageField(upload_to="photos/%y/")
    class Meta:
        verbose_name="Штаны"
        verbose_name_plural="Штаны"


class Tshirt(models.Model):
    name = models.CharField(max_length=30)
    model = models.CharField(max_length=30)
    price = models.IntegerField(blank=True)
    photo = models.ImageField(upload_to="photos/%y/")
    class Meta:
        verbose_name="Футболка"
        verbose_name_plural="Футболка"

class Blouse(models.Model):
    name = models.CharField(max_length=30)
    model = models.CharField(max_length=30)
    price = models.IntegerField(blank=True)
    photo = models.ImageField(upload_to="photos")
    class Meta:
        verbose_name="Кофта"
        verbose_name_plural="Кофта"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_id': self.pk})

