from django.http import JsonResponse
from django.shortcuts import render

from mainsite.forms import QueryForm
from mainsite.models import Chat, Message, Service


def index(request):
    services = Service.objects.all()
    return render(request, "index.html", {"services": services})


def privacy_policy(request):
    return render(request, "privacy_policy.html")


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
            if link_message_to_chat(chat_id, message_text):
                return JsonResponse({"msg": "OK"})
            else:
                return JsonResponse({"msg": "Cannot create Message"})
        except Exception as e:
            return JsonResponse({"error": e})


def queries(request, chat_id):
    if request.method == "GET":
        try:
            chat = Chat.objects.get(pk=chat_id, user=request.user)
        except:
            return render(request, "query.html", {"allowed": False})
        else:
            messages = Message.objects.filter(chat=chat)
        return render(request, "query.html", {"messages": messages, "allowed": True})


def link_message_to_chat(chat_id, message_text):
    fetched_chat = Chat.objects.get(pk=chat_id)
    new_message = Message(chat=fetched_chat, message_text=message_text)
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
