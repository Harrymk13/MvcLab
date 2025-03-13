from django.contrib import admin
from django.urls import include, path  # Musi być 'include'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('polls/', include('polls.urls')),  # Upewnij się, że polls.urls istnieje!
]
