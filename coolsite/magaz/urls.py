from django.urls import path

from .views import *

urlpatterns=[
    path('',index, name='home'),
    path('info/',information, name='info'),
    path('cat/',categori, name='cat'),
    path('feed/',feedback, name='feedback'),
    path('post/<int:post_id>/', show_post, name='post'),
]