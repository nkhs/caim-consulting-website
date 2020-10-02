from django.db import IntegrityError
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render

from mainsite.forms import QueryForm
from mainsite.models import Advisor, Chat, Message, Subscriber


def index(request):
    return render(request, "index.html")


def privacy_policy(request):
    return render(request, "privacy_policy.html")


def disclaimer(request):
    return render(request, "disclaimer.html")


def services(request):
    return render(request, "services.html")


def advisory_board(request, member):
    advisor = get_object_or_404(Advisor, slug=member)
    return render(request, "advisor_bio.html", {"advisor": advisor})


def developers(request):
    return render(request, "developers.html")


def contactform(request):
    if request.method == "POST":
        form = QueryForm(request.POST)
        user = request.user
        if form.is_valid():
            if link_chat_to_message(form.cleaned_data, user):
                return JsonResponse({"msg": "OK"})
            else:
                return JsonResponse({"msg": "Cannot create Chat"})
        else:
            return JsonResponse({"msg": "Invalid Form"})


def messageinput(request):
    if request.method == "POST":
        try:
            chat_id = request.POST.get("chat")
            message_text = request.POST.get("message")
            if request.user.is_staff:
                admin_msg = True
            else:
                admin_msg = False
            if link_message_to_chat(chat_id, message_text, admin_msg):
                return JsonResponse({"msg": "OK"})
            else:
                return JsonResponse({"msg": "Cannot create Message"})
        except Exception as e:
            return JsonResponse({"error": e})


def subscription(request):
    if request.method == "POST":
        try:
            email = request.POST.get("email")
            if email:
                subs = Subscriber(email=email)
                subs.save()
        except IntegrityError:
            print("Email already in subscriptions")
        except Exception as e:
            print(e)
        return redirect(index)


def chats(request, chat_id):
    if request.method == "GET":
        try:
            chat = get_object_or_404(Chat, pk=chat_id, user=request.user)
            allowed = True
        except Exception as e:
            chat = get_object_or_404(Chat, pk=chat_id)
            allowed = request.user.is_staff
        if allowed:
            messages = Message.objects.filter(chat=chat)
            return render(
                request, "query.html", {"messages": messages, "allowed": allowed}
            )
        else:
            return render(request, "query.html", {"allowed": allowed})


def link_message_to_chat(chat_id, message_text, admin_msg=False):
    fetched_chat = Chat.objects.get(pk=chat_id)
    new_message = Message(
        chat=fetched_chat, message_text=message_text, by_admin=admin_msg
    )
    new_message.save()
    return True


def link_chat_to_message(data, user):
    subject = data["subject"]
    message = data["message"]
    service = data["service"]
    chat = Chat(user=user, subject=subject, service=service)
    chat.save()
    message = Message(chat=chat, message_text=message)
    message.save()
    return True
