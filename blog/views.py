from django.shortcuts import render

from blog.models import BlogPost, Category

# Create your views here.
def blog_index(request):
    categories = Category.objects.all()
    return render(request, "blog_index.html", {"categories": categories})


def blog_page(request, blog_id):
    blog = BlogPost.objects.get(pk=blog_id)
    return render(request, "blog_page.html", {"blog": blog})


def catg_page(request, catg_id):
    category = Category.objects.get(pk=catg_id)
    blogs_in_category = BlogPost.objects.filter(category=category)
    return render(
        request,
        "category_page.html",
        {"blogs_in_category": blogs_in_category, "category": category},
    )
