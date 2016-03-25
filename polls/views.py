from django.http import HttpResponse
from polls.models import Item
from django.template.loader import get_template 
from django.shortcuts import render_to_response, render, redirect
from django.template import Context
from django.core.paginator import Paginator
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.core.urlresolvers import reverse
from paypal.standard.forms import PayPalPaymentsForm

def catalog(request, number_page = 1):
    all_Items = Item.objects.all()
    current_page = Paginator(all_Items, 6)
    ps = get_template('polls/catalog.html')
    html = ps.render({'Items' : current_page.page(number_page)}) 
    return HttpResponse(html)


def index(request):
    html = "aaa"

    return HttpResponse(html)

def item(request, Item_id = 1):
    return render_to_response('polls/item.html', {'Item' : Item.objects.get(id = Item_id)})
    #'username': auth.get_user(request).username

def mycart(request):
    ps = get_template('polls/mycart.html')
    html = ps.render()
    return HttpResponse(html)

def home(request):
    """
    Home page with auth links.
    """
    print(request.user.is_authenticated())
    if request.user.is_authenticated():
        return HttpResponse("{0} <a href='/accounts/logout'>exit</a>".format(request.user))
    else:
        return HttpResponse("<a href='/login/vk-oauth2/'>login with VK</a>")


def account_profile(request):
    """
    Show user greetings. Only for logged in users.
    """
    return HttpResponse("Hi, {0}! Nice to meet you.".format(request.user.first_name))


def account_logout(request):
    """
    Logout and redirect to the main page.
    """
    logout(request)
    return redirect('/')  

def paypal_success(request):
    """
    Tell user we got the payment.
    """
    return HttpResponse("Money is mine. Thanks.")


def paypal_pay(request):
    """
    Page where we ask user to pay with paypal.
    """
    paypal_dict = {
        "business": "b2239543-facilitator@trbvn.com",
        "amount": "100.00",
        "currency_code": "RUB",
        "item_name": "products in socshop",
        "invoice": "INV-00001",
        "notify_url": reverse('paypal-ipn'),
        "return_url": "http://localhost:8000/payment/success/",
        "cancel_return": "http://localhost:8000",
        "custom": str(request.user.id)
    }

    # Create the instance.
    form = PayPalPaymentsForm(initial=paypal_dict)
    context = {"form": form, "paypal_dict": paypal_dict}
    return render(request, "polls/payment.html", context)


pass