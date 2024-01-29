from django.contrib import admin
from .models import Messages


class MessagesAdmin(admin.ModelAdmin):
    list_display = ('pk', 'sender', 'receiver', 'subject', 'creation_date', 'is_read')
    ordering = ['pk']

    class Meta:
        model = Messages


admin.site.register(Messages, MessagesAdmin)
