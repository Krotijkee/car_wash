from django.urls import path
from . import views

urlpatterns = [
    path(r'', views.home),
    path('contact_1/<str:loc>', views.contact_1),
    path('reviews', views.reviews),
    path('home', views.home),
    path('license', views.license),
    path('clients', views.clients)
]
