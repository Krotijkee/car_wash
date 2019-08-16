from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from .models import Review
from django.utils.timezone import now
import smtplib


def home(request):
    return render(request, "car_wash/home.html")

#contacts package
def contact_1(request, loc):
    return render(request, "car_wash/contacts/{}".format(loc))

#about_us package
def reviews(request):

    posts = Review.objects.all().order_by('-id')[:3]
    context = {
        'posts' : posts
    }
    return render(request, "car_wash/about_us/reviews.html",context)

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

#gallery package

def gallery(request, loc):
    return render(request, "car_wash/gallery/{}".format(loc))

#handler
def main_get(request):

    if request.POST:

        # create message object instance
        msg = MIMEMultipart()

        message = "From:" + " " + request.POST["email"] + " " + "Message:" + " " + request.POST["message"]

        # setup the parameters of the message
        password = "fregat"
        msg['From'] = "fregatwasher@yandex.ru"
        msg['To'] = "fregatwasher@yandex.ru"
        msg['Subject'] = "Обратная связь"

        # add in the message body
        msg.attach(MIMEText(message, 'plain'))

        # create server
        server = smtplib.SMTP('smtp.yandex.ru: 587')

        server.starttls()

        # Login Credentials for sending the mail
        server.login(msg['From'], password)

        # send the message via the server.
        server.sendmail(msg['From'], msg['To'], msg.as_string())

        server.quit()

        print
        "successfully sent email to %s:" % (msg['To'])
        return HttpResponse('Ваше сообщение отправлено')
    else:
        return HttpResponse('Ошибка')


#review send

def send_review(request):
    if request.POST:
        req_name = request.POST['name']
        req_text = request.POST['text']
        req_email = request.POST['email']

        # print(req_name)
        # print(req_text)
        # print(req_email)
        new_review = Review(date = now(), name = req_name, email = req_email,text = req_text)
        new_review.save()


        return HttpResponse('Ваш отзыв успешно размещён!')
    else:
        return HttpResponse('Ошибка')

