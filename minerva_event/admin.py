from django.contrib import admin, messages

# Register your models here.
from django.db import models
from django.http import HttpResponseRedirect
from django.shortcuts import render

from minerva_event.models import Person, Event, EventLoc, Attendance, MassAttendanceProxy
from minerva_event.views import MassAttendanceForm


class EventAdmin(admin.ModelAdmin):
    list_display = ['title', 'eventdate', 'eventduration', 'location_name']
    search_fields = ['title']

    def location_name(self,instance):
        return instance.eventlocation.name


admin.site.register(Event,EventAdmin)

class PersonAdmin(admin.ModelAdmin):
    list_display = ['uniqueID', 'name', 'phno']
    search_fields = ['name', 'uniqueID']

admin.site.register(Person, PersonAdmin)

class EventLocAdmin(admin.ModelAdmin):
    list_display = ['name', 'address']
    search_fields = ['name', 'address']

admin.site.register(EventLoc, EventLocAdmin)

class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('event', 'personid', 'personname')
    list_filter = ('event__title',)

    def personid(self,instance):
        return instance.attendee.uniqueID

    def personname(self,instance):
        return instance.attendee.name

admin.site.register(Attendance,AttendanceAdmin )






class MassAttendanceAdmin(admin.ModelAdmin):
    pass


admin.site.register(MassAttendanceProxy,MassAttendanceAdmin)





