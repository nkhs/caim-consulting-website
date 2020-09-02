from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from accounts.forms import SignUpForm
from mainsite.models import Chat, Service


@login_required
def profile(request):
    if request.user.is_staff:
        chats = Chat.objects.all()
    else:
        chats = Chat.objects.filter(user=request.user)
    services = Service.objects.all()
    resolved_chats = chats.filter(resolved=True)
    unresolved_chats = chats.filter(resolved=False)
    return render(
        request,
        "profile.html",
        {
            "unresolved_chats": unresolved_chats,
            "resolved_chats": resolved_chats,
            "services": services,
        },
    )


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
