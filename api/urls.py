from django.urls import include, path
from rest_framework.routers import DefaultRouter

from . import views

# Using the Router for the Employeedata
# router = DefaultRouter()
# router.register("employees", views.EmployeeViewset, basename="employee")

urlpatterns = [
    # # API URL paths for the student App
    # path("students/", views.studentsView),
    # path("students/<int:pk>", views.StudentDetailView),
    # API URL paths for the Employee App
    # path("employees/", views.Employees.as_view()),
    # path("employees/<int:pk>", views.EmployeeDetailed.as_view()),
    # Viewset urls
    # path("", include(router.urls)),
    # Blog App URLS
    path("blogs/", views.BlogView.as_view()),
    path("comments/", views.CommentView.as_view()),
    # Blog App URLS based on primary key operations
    path("blogs/<int:pk>", views.BlogDetailedView.as_view()),
    path("comments/<int:pk>", views.CommentDetailedView.as_view()),
]
