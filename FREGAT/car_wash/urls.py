from django.urls import path
from . import views

urlpatterns = [
    path(r'', views.index),
    path('contact_1/<str:loc>', views.contact_1),
    path('reviews', views.reviews)
]
