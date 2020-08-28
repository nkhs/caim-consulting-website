from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from accounts.forms import SignUpForm
from mainsite.models import Chat, Service


@login_required
def profile(request):
    if request.user.is_staff:
        queries = Chat.objects.all()
    else:
        queries = Chat.objects.filter(user=request.user)
    services = Service.objects.all()
    return render(request, "profile.html", {"queries": queries, "services": services})


def sign_up(request):
    context = {}
    form = SignUpForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("profile")
    context["form"] = form
    return render(request, "registration/sign_up.html", context)
