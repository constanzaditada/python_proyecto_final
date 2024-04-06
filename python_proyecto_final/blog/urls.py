from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog_list, name='blog_list'),
    path('about/', views.about_me, name='about_me'),
    path('send_message/', views.send_message, name='send_message'),
    path('inbox/', views.inbox, name='inbox'),
    path('message_detail/<int:message_id>/', views.message_detail, name='message_detail'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('profile/', views.profile, name='profile'),
    path('libros/', views.libro_list, name='libro_list'),
    path('libro/<int:pk>/', views.libro_detalle, name='libro_detalle'),
    path('libro/nuevo/', views.libro_nuevo, name='libro_nuevo'),
    path('libro/<int:pk>/editar/', views.libro_editar, name='libro_editar'),
    path('libro/<int:pk>/eliminar/', views.libro_eliminar, name='libro_eliminar'),
]