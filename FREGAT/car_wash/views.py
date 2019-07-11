from django.shortcuts import render


def index(request):
    return render(request, "car_wash/index2.html")


