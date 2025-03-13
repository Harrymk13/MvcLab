from django.urls import path

from . import views  # Importuje widoki z polls/views.py

urlpatterns = [
    path('', views.index, name='index'),  # Domyślna strona dla polls/
]
