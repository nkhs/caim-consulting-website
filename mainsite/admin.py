from django.contrib import admin
from mainsite.models import Advisor, Chat, Client, Message, Service, Subscriber


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    pass


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = (
        "disp_priority",
        "name",
        "client_url",
    )
    search_fields = ("name",)


@admin.register(Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    list_display = (
        "pk",
        "datetime",
        "email",
    )
    search_fields = ("email",)

    def has_change_permission(self, request, obj=None):
        return False


@admin.register(Advisor)
class AdvisorAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "disp_priority",
        "position",
        "linkedin",
    )
    search_fields = ("name",)


@admin.register(Chat)
class ChatAdmin(admin.ModelAdmin):
    actions = ["mark_as_resolved", "mark_as_unresolved"]
    list_display = (
        "pk",
        "created_at",
        "user",
        "contact_platform",
        "mobile_num_chat",
        "subject",
        "service",
        "resolved",
    )
    list_filter = ("resolved", "service")
    search_fields = ("subject", "user")

    def mark_as_resolved(self, request, queryset):
        queryset.update(resolved=True)

    mark_as_resolved.short_description = "Mark selected chats as resolved"

    def mark_as_unresolved(self, request, queryset):
        queryset.update(resolved=False)

    mark_as_unresolved.short_description = "Mark selected chats as unresolved"

    def has_add_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = (
        "chat__subject",
        "offset",
        "by_admin",
        "chat__resolved",
    )
    list_filter = ("chat__resolved",)
    search_fields = ("by_admin", "chat__subject")

    def chat__subject(self, obj):
        return obj.chat.subject

    def chat__resolved(self, obj):
        return obj.chat.resolved

    chat__resolved.admin_order_field = "chat__resolved"
    chat__subject.admin_order_field = "chat__subject"
    chat__resolved.boolean = True

    def has_change_permission(self, request, obj=None):
        return False
