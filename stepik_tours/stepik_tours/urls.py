from django.contrib import admin
from django.urls import path

from tours.views import MainView, DepartureView, TourView

urlpatterns = [
    path('', MainView),
    path('/departure/<str:departure>/', DepartureView),
    path('/tour/<int:id>/', TourView),
    path('admin/', admin.site.urls),
]
