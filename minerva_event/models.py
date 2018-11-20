from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class EventLoc(models.Model):
    name = models.CharField(max_length=80)
    address = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = "Event Location"


class Event(models.Model):
    title = models.CharField(max_length=80)
    eventdate = models.DateTimeField(verbose_name="Event Date")
    eventduration = models.IntegerField(verbose_name="Event Duration")
    eventlocation = models.ForeignKey(EventLoc, on_delete=models.CASCADE, verbose_name="Event Location")

    def __str__(self):
        return str(self.title)

    class Meta:
        verbose_name = "Event"


class Person(models.Model):
    uniqueID = models.CharField(max_length=20, verbose_name="USN or FacultyID")
    name = models.CharField(max_length=60)
    phno = PhoneNumberField(null=True, blank=True, verbose_name="Phone Number")

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = "Person"


class Attendance(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    attendee = models.ForeignKey(Person, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Attendance"

class MassAttendanceProxy(Attendance):
    class Meta:
        app_label = 'minerva_event'  # This is the app that the form will exist under
        verbose_name_plural = 'Mass Attendance'  # This is the name used in the link text

        abstract = False
        proxy = True


