from django.shortcuts import render


def index(request):
    return render(request, "car_wash/wrapper.html")

def contact_1(request,loc):
    return render(request, "car_wash/{}".format(loc))

def reviews(request):
    return render(request, "car_wash/reviews.html")



