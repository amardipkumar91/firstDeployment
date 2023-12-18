from django.urls import path,include
from api import views

urlpatterns = [
    path('company/',views.CompanyAPI.as_view()),
    path('company/<int:pk>/',views.CompanyAPI.as_view()),
    path('employee/',views.EmployeeAPI.as_view()),
    path('employee/<int:pk>/',views.EmployeeAPI.as_view())
]
# (?P<id>[0-9]+)