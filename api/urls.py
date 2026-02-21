from django.urls import include, path
from rest_framework.routers import DefaultRouter

from . import views

# Using the Router
router = DefaultRouter()
router.register("employees", views.EmployeeViewset, basename="employee")

urlpatterns = [
    # # API URL paths for the student App
    # path("students/", views.studentsView),
    # path("students/<int:pk>", views.StudentDetailView),
    # # API URL paths for the Employee App
    # path("employees/", views.Employees.as_view()),
    # path("employees/<int:pk>", views.EmployeeDetailed.as_view()),
    
    # Viewset urls
    path("", include(router.urls))

    
]
