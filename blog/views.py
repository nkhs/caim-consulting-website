from django.shortcuts import get_object_or_404, render

from blog.models import BlogPost, Category


# Create your views here.
def blog_index(request):
    categories = Category.objects.all()
    latest_3_blogs = BlogPost.objects.all().order_by("-id")[:3]
    return render(
        request,
        "blog_index.html",
        {"categories": categories, "latest_3_blogs": latest_3_blogs},
    )


def blog_page(request, blog_id):
    blog = get_object_or_404(BlogPost, pk=blog_id)
    return render(request, "blog_page.html", {"blog": blog})


def catg_page(request, catg_id):
    category = get_object_or_404(Category, pk=catg_id)
    blogs_in_category = BlogPost.objects.filter(category=category, draft=False)
    return render(
        request,
        "category_page.html",
        {"blogs_in_category": blogs_in_category, "category": category},
    )
