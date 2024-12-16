from django.urls import path
from . import views

urlpatterns = [
    path('course_outcomes/', views.outcomes, name='outcomes'),
    path('course_outcomes/insertco/',views.insertco, name='insertco'),
    path('view_co/',views.view_co,name='view_co'),
]