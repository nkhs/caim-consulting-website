from django.shortcuts import render
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

from accounts.forms import SignUpForm
from mainsite.models import Chat


@login_required
def profile(request):
    print(request.user)
    queries = Chat.objects.filter(user=request.user)
    return render(request, "profile.html", {"queries": queries})


def sign_up(request):
    context = {}
    form = SignUpForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            user = form.save()
            login(request, user)
            return render(request, "profile.html")
    context["form"] = form
    return render(request, "registration/sign_up.html", context)
