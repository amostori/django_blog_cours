from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    category_name = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        # self oznacza Category. Stąd self.category_name to inaczej
        # Category.category_name
        return self.category_name
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
  
STATUS_CHOICES = (
    ('draft', 'Draft'),
    ('published', 'Published'),
)     
class Blog(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=150, unique=True)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    featured_image = models.ImageField(upload_to='uploads/%Y/%m/%d/')
    short_description = models.TextField(max_length=500)
    blog_body = models.TextField(max_length=2000)
    status = models.CharField( max_length=20, choices=STATUS_CHOICES, default='draft')
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        
        return self.title