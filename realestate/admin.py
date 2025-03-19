from django.contrib import admin
from .models import CustomUser, Property, Appointment, Agent, Transaction

admin.site.register(CustomUser)
admin.site.register(Property)
admin.site.register(Transaction)

@admin.register(Agent)
class AgentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone')

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'property', 'agent', 'date', 'time')
    list_filter = ('date', 'property', 'agent')
    search_fields = ('name', 'email', 'phone', 'property__title', 'agent__name')
