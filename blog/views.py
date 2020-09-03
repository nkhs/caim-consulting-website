from django.shortcuts import get_object_or_404, render

from blog.models import Category, Publication


# Create your views here.
def publication_index(request):
    categories = Category.objects.all()
    latest_3_publications = Publication.objects.all().order_by("-id")[:3]
    return render(
        request,
        "publication_index.html",
        {"categories": categories, "latest_3_publications": latest_3_publications},
    )


def publication_page(request, publication_id):
    publication = get_object_or_404(Publication, pk=publication_id)
    return render(request, "publication_page.html", {"publication": publication})


def catg_page(request, catg_id):
    category = get_object_or_404(Category, pk=catg_id)
    publications_in_category = Publication.objects.filter(
        category=category, draft=False
    )
    return render(
        request,
        "category_page.html",
        {"publications_in_category": publications_in_category, "category": category},
    )
