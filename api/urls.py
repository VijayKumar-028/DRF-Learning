from django.urls import path

from . import views

urlpatterns = [
    # API URL paths for the student App
    path("students/", views.studentsView),
    path("students/<int:pk>", views.StudentDetailView),
    # API URL paths for the Employee App
    path("employees/", views.Employees.as_view()),
    path("employees/<int:pk>", views.EmployeeDetailed.as_view()),
]
