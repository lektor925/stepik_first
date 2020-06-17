from django.contrib import admin
from django.urls import path

from tours.views import main_view, departure_view, tour_view

urlpatterns = [
    path('', main_view, name='home'),
    path('departure/<str:departure>/', departure_view),
    path('tour/<int:id>/', tour_view),
    path('admin/', admin.site.urls),
]
