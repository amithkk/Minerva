#  Copyright (c) 2018 - Amith K K
#  Released under the GNU GPLv3 License
#

from django import  forms
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from minerva_event.models import MassAttendanceProxy


class MassAttendanceForm(forms.Form):
    attendance_list = forms.CharField()

    class Meta:
        fieldsets = (('att', {'fields': ('attendance_list',), 'legend': ''}),)

def mass_attendance(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = MassAttendanceForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = MassAttendanceForm()

    data = {
            'opts': MassAttendanceProxy._meta,
            'change': False,
            'is_popup': False,
            'save_as': False,
            'add': False,
            'has_view_permission': True,
            'has_editable_inline_admin_formsets': False,
            'has_delete_permission': False,
            'has_add_permission': False,
            'has_change_permission': True,
            'adminform': form}

    return render(request, 'admin/change_form.html', data)
