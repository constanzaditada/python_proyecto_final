from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView, LogoutView
from .models import Blog
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Message

def blog_list(request):
    blogs = Blog.objects.all()
    return render(request, 'blog/blog_list.html', {'blogs': blogs})

def blog_detail(request, blog_id):
    blog = Blog.objects.get(pk=blog_id)
    return render(request, 'blog/blog_detail.html', {'blog': blog})

def about_me(request):
    return render(request, 'blog/about_me.html')

class SignUpView(CreateView):
    template_name = 'registration/signup.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        form.save()
        # Lógica para crear el perfil
        return redirect(self.success_url)
    
@login_required
def send_message(request, recipient_id):
    recipient = get_object_or_404(User, pk=recipient_id)
    if request.method == 'POST':
        return HttpResponseRedirect(reverse('inbox'))
    return render(request, 'blog/send_message.html', {'recipient': recipient})

@login_required
def inbox(request):
    messages = Message.objects.filter(recipient=request.user)
    return render(request, 'blog/inbox.html', {'messages': messages})

@login_required
def message_detail(request, message_id):
    message = get_object_or_404(Message, pk=message_id)
    return render(request, 'blog/message_detail.html', {'message': message})

def send_message(request):
    # Lógica para enviar un mensaje
    return render(request, 'blog/send_message.html')

def inbox(request):
    messages = Message.objects.filter(recipient=request.user)
    return render(request, 'blog/inbox.html', {'messages': messages})

def message_detail(request, message_id):
    message = Message.objects.get(pk=message_id)
    return render(request, 'blog/message_detail.html', {'message': message})

def inbox(request):
    messages = Message.objects.filter(recipient=request.user)
    return render(request, 'tu_app/inbox.html', {'messages': messages})

@login_required
def profile(request):
    user = request.user
    return render(request, 'profile.html', {'user': user})

def libro_list(request):
    libros = Libro.objects.all()
    return render(request, 'libro/list.html', {'libros': libros})

def libro_detalle(request, pk):
    libro = get_object_or_404(Libro, pk=pk)
    return render(request, 'libro/detalle.html', {'libro': libro})

def libro_nuevo(request):
    if request.method == 'POST':
        form = LibroForm(request.POST)
        if form.is_valid():
            libro = form.save()
            return redirect('libro_detalle', pk=libro.pk)
    else:
        form = LibroForm()
    return render(request, 'libro/nuevo.html', {'form': form})

def libro_editar(request, pk):
    libro = get_object_or_404(Libro, pk=pk)
    if request.method == 'POST':
        form = LibroForm(request.POST, instance=libro)
        if form.is_valid():
            libro = form.save()
            return redirect('libro_detalle', pk=libro.pk)
    else:
        form = LibroForm(instance=libro)
    return render(request, 'libro/editar.html', {'form': form, 'libro': libro})

def libro_eliminar(request, pk):
    libro = get_object_or_404(Libro, pk=pk)
    if request.method == 'POST':
        libro.delete()
        return redirect('libro_list')
    return render(request, 'libro/confirmar_eliminar.html', {'libro': libro})

def libro_list(request):
    libros = Libro.objects.all()

    # Obtener el término de búsqueda si está presente en la solicitud GET
    query = request.GET.get('q')
    if query:
        libros = libros.filter(titulo__icontains=query)
    return render(request, 'blog/libro_list.html', {'libros': libros})