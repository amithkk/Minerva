#  Copyright (c) 2018 - Amith K K
#  Released under the GNU GPLv3 License
#

from authtools.models import User
from django.contrib import auth
from django.shortcuts import render, redirect


def student_login(request):
    student = User.objects.get(email='nmit_student@nmit.ac.in')
    auth.login(request,student)
    return redirect('/minerva_core/publication/')
