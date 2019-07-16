from django.shortcuts import render


def home(request):
    return render(request, "car_wash/home.html")

#contacts package
def contact_1(request, loc):
    return render(request, "car_wash/contacts/{}".format(loc))

#about_us package
def reviews(request):
    return render(request, "car_wash/about_us/reviews.html")

def license(request):
    return render(request, "car_wash/about_us/license.html")

def clients(request):
    return render(request, "car_wash/about_us/clients.html")


