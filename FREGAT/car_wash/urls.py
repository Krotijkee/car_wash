from django.urls import path,include
from . import views

urlpatterns = [
    path(r'', views.home),
    path('contact_1/<str:loc>', views.contact_1),
    path('reviews', views.reviews),
    path('home', views.home),
    path('license', views.license),
    path('clients', views.clients),
    path('w-contact', views.w_contact),
    path('nano', views.nano),
    path('chemical', views.chemical),
    path('price', views.price),
    path('actions', views.actions),
    path('gruzovik', views.gruzovik),
    path('gallery/<str:loc>', views.gallery),
    path('main_get', views.main_get, name='main_get'),
    path('send_review', views.send_review, name='send_review')

]
