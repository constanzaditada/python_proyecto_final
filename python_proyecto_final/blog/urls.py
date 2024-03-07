from django.urls import path
from . import views

urlpatterns = [
    # URL para la lista de blogs
    path('', views.blog_list, name='blog_list'),
    path('about/', views.about_me, name='about_me'),
    path('send_message/', views.send_message, name='send_message'),
    path('inbox/', views.inbox, name='inbox'),
    path('message_detail/<int:message_id>/', views.message_detail, name='message_detail'),
]