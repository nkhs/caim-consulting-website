from django.contrib import admin
from mainsite.models import Query


@admin.register(Query)
class QueryAdmin(admin.ModelAdmin):
    actions = ["mark_as_resolved", "mark_as_unresolved"]
    list_display = (
        "date_time",
        "name",
        "email",
        "subject",
        "message",
        "resolved",
    )
    list_filter = ("resolved", "email")

    def mark_as_resolved(self, request, queryset):
        queryset.update(resolved=True)

    mark_as_resolved.short_description = "Mark selected queries as resolved"

    def mark_as_unresolved(self, request, queryset):
        queryset.update(resolved=False)

    mark_as_unresolved.short_description = "Mark selected queries as unresolved"

    def has_change_permission(self, request, obj=None):
        return False
