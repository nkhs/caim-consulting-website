from django.shortcuts import render

# Create your views here.
def blog_index(request):
    return render(request, "blog_index.html")