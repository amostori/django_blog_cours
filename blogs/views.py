from django.shortcuts import render, get_object_or_404, redirect

from blogs.models import Blog, Category

def posts_by_category(request, category_id):
    posts = Blog.objects.filter(category=category_id, status='published')
    try:
        category = Category.objects.get(id=category_id)
    except Category.DoesNotExist:
        return redirect('home')
    # category = get_object_or_404(Category, id=category_id)
    context = {
        'posts': posts,
        'category': category
    }
    return render(request, 'posts_by_category.html', context)
