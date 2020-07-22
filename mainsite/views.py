from django.http import JsonResponse
from django.shortcuts import render

from mainsite.forms import QueryForm


def index(request):
    return render(request, "index.html")


def contactform(request):
    if request.method == "POST":
        form = QueryForm(request.POST)
        if form.is_valid():
            query = form.save(commit=False)
            query.save()
            return JsonResponse({"msg": "OK"})
        else:
            return JsonResponse({"msg": "Invalid Form"})
