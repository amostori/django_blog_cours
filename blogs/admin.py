from django.contrib import admin

# Register your models here.
from .models import Blog, Category

class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    # przecinek jest konieczny bo to tuple, a tuple nie może zawierać jednego
    # elementu, wiec trzeba dodać przecinek
    list_display = ('title', 'category', 'author','status','is_featured', )
    search_fields = ('id', 'title', 'category__category_name', 'status')
    list_editable= ('status', 'is_featured')
    # list editable oznacza, że będzie można edytować pola podane z poziomu
    # list_display
    
admin.site.register(Category)
admin.site.register(Blog, BlogAdmin)
