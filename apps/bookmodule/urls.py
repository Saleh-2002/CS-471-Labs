from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.index),
    path('index2/<int:val1>/', views.index2),  # passing an integer value to the view function
    path('<int:bookId>', views.viewbook) 
]