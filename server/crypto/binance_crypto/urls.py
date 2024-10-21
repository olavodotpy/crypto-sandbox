from django.urls import path

from . import views

# URLs do /app

urlpatterns = [
    path('usuarios/', views.DataTrigger.as_view()),
]