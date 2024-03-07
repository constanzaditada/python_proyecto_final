from django.db import models
from django.contrib.auth.models import User

class Blog(models.Model):
    title = models.CharField(max_length=100, help_text="New York Fashion Week")
    subtitle = models.CharField(max_length=200, blank=True, help_text="El mejor año de la moda")
    body = models.TextField(help_text="El cuerpo del blog, donde se encuentra el contenido principal.")
    author = models.ForeignKey(User, on_delete=models.CASCADE, help_text="El autor del blog, enlazado al modelo de usuario predeterminado de Django.")
    date = models.DateTimeField(auto_now_add=True, help_text="La fecha de creación del blog, con valor predeterminado establecido en la fecha y hora actuales.")
    image = models.ImageField(upload_to='blog_images/', help_text="Una imagen asociada al blog, que se almacenará en la carpeta blog_images/ dentro del directorio de medios de Django.")

    def __str__(self):
        return self.title

class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_messages')
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Message from {self.sender} to {self.receiver}'

    class Meta:
        ordering = ['-timestamp']