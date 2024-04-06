from django.test import TestCase

# Create your tests here.
import unittest
from django.test import TestCase
from django.urls import reverse
from .models import Blog

class BlogTestCase(TestCase):
    def setUp(self):
        self.blog = Blog.objects.create(
            title='Título de prueba',
            subtitle='Subtítulo de prueba',
            body='Contenido de prueba',
            author='Autor de prueba',
            date='2024-04-06',
            image='ruta/imagen.jpg'
        )

    def test_blog_creation(self):
        self.assertEqual(self.blog.title, 'Título de prueba')
        self.assertEqual(self.blog.subtitle, 'Subtítulo de prueba')
        # Agrega más aserciones para verificar otros campos del blog

if __name__ == '__main__':
    unittest.main()