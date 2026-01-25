from django.http import HttpResponse
from django.shortcuts import render


def students(request):
    students = [{"id": 1, "name": "john doe", "age": 20}]
    return HttpResponse(students)
