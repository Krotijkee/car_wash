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

#auto_washing package

def w_contact(request):
    return render(request, "car_wash/auto_washing/w_contact.html")

def nano(request):
    return render(request, "car_wash/auto_washing/nano.html")

def chemical(request):
    return render(request, "car_wash/auto_washing/chemical.html")

def gruzovik(request):
    return render(request, "car_wash/auto_washing/gruz.html")

#price package

def price(request):
    return render(request, "car_wash/price/pricelist.html")

#actions package

def actions(request):
    return render(request, "car_wash/actions/actions.html")

