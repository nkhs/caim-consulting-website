from django.contrib import admin

from mainsite.models import Chat, Message


@admin.register(Chat)
class ChatAdmin(admin.ModelAdmin):
    actions = ["mark_as_resolved", "mark_as_unresolved"]
    list_display = (
        "pk",
        "created_at",
        "creator_name",
        "creator_email",
        "subject",
        "resolved",
    )
    list_filter = ("resolved",)
    search_fields = ("subject", "creator_email")

    def mark_as_resolved(self, request, queryset):
        queryset.update(resolved=True)

    mark_as_resolved.short_description = "Mark selected queries as resolved"

    def mark_as_unresolved(self, request, queryset):
        queryset.update(resolved=False)

    mark_as_unresolved.short_description = "Mark selected queries as unresolved"

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
