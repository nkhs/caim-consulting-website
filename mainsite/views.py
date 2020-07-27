from django.http import JsonResponse
from django.shortcuts import render

from mainsite.forms import QueryForm
from mainsite.models import Chat, Message


def index(request):
    return render(request, "index.html")


def contactform(request):
    if request.method == "POST":
        form = QueryForm(request.POST)
        if form.is_valid():
            if link_chat_to_message(form.cleaned_data):
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
        messages = Message.objects.filter(chat__pk=chat_id)
        return render(request, "query.html", {"messages": messages})


def link_message_to_chat(chat_id, message_text):
    fetched_chat = Chat.objects.get(pk=chat_id)
    new_message = Message(chat=fetched_chat, message_text=message_text)
    new_message.save()
    return True


def link_chat_to_message(data):
    name = data["name"]
    email = data["email"]
    subject = data["subject"]
    message = data["message"]
    chat = Chat(creator_name=name, creator_email=email, subject=subject)
    chat.save()
    message = Message(chat=chat, message_text=message)
    message.save()
    return True
