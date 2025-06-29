from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('guess/', views.guess, name='guess'),
    path('restart/', views.restart_game, name='restart'),  # ✅ Restart functionality
]
