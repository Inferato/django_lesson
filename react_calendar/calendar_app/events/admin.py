from datetime import datetime
from typing import Any
from django.db.models import Q
from django.db.models.query import QuerySet
import pytz
from django.contrib import admin
from .models import Event

utc = pytz.UTC


class EventStatuses:
    upcoming = "Upcoming event"
    in_progress = "Event in progress"
    past_due = "Event is past due"


class CompletionFilter(admin.SimpleListFilter):
    title = 'Completion status'
    parameter_name = 'is_completed'

    def lookups(self, request, model_admin):
        return [
            ('upcoming', EventStatuses.upcoming),
            ('in_progress', EventStatuses.in_progress),
            ('past_due', EventStatuses.past_due),
        ]

    def queryset(self, request: Any, queryset: QuerySet[Any]) -> QuerySet[Any] | None:
        today = utc.localize(datetime.now())
        if self.value() == 'upcoming':
            return queryset.filter(start_date__gte=today)
        if self.value() == 'in_progress':
            return queryset.filter(Q(start_date__lt=today) & Q(end_date__gt=today))
        if self.value() == 'past_due':
            return queryset.filter(end_date__lt=today)


class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'event_status', 'completion', 'is_completed')
    list_editable = ('is_completed', )
    list_filter = ('end_date', CompletionFilter)
    search_fields = ('title', 'description',)
    actions = ['complete_event']
    readonly_fields = ('is_completed',)
    add_form_template = 'admin/add_form.html'
    list_per_page = 3

    def event_status(self, obj):
        today = utc.localize(datetime.now())
        start_date = obj.start_date
        end_date = obj.end_date
        if start_date > today:
            return EventStatuses.upcoming
        if start_date < today:
            if end_date > today:
                return EventStatuses.in_progress
            else:
                return EventStatuses.past_due
    event_status.short_description = 'Event status'

    def completion(self, obj):
        return 'Completed' if obj.is_completed else "In progress"
    completion.short_description = 'Completion status'

    def complete_event(self, request, queryset):
        for event in queryset:
            event.is_completed = True
            event.save(update_fields=['is_completed'])
        


admin.site.register(Event, EventAdmin)

