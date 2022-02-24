from django.contrib import admin
from support.models import Support,Ticket
# Register your models here.


class SupportInline(admin.TabularInline):
    model = Support

@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    inlines = [SupportInline,]
