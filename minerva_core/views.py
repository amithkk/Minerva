from django.contrib import auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


def student_login(request):
    student = User.objects.get(username='nmit_student')
    auth.login(request,student)
    return redirect('/minerva_core/publication/')

