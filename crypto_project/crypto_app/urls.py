from django.urls import path

from . import views


# URLs do /app
urlpatterns = [
    path('consulting/', views.DataTrigger.as_view()),
]