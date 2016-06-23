from django.http import HttpResponse
from polls.models import *
from django.template.loader import get_template 
from django.shortcuts import render_to_response, render, redirect
from django.template import Context
from django.core.paginator import Paginator
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.core.urlresolvers import reverse
from paypal.standard.forms import PayPalPaymentsForm
import random

def catalog(request, number_page = 1):
    all_Items = Item.objects.all()
    current_page = Paginator(all_Items, 6)
    ps = get_template('polls/catalog.html')

    cart_id = request.COOKIES.get("cart")
    try:
        cart = Cart.objects.filter(id = cart_id)[0]
    except:
        cart = Cart()
        cart.save()
    
    html = ps.render({'Items' : current_page.page(number_page), 'Cart_items' : cart.items.all()})
    res = HttpResponse(html)
    res.set_cookie("cart", cart.id)
    return res


def index(request):
    html = "aaa"

    return HttpResponse(html)

def item(request, Item_id = 1):
    return render_to_response('polls/item.html', {'Item' : Item.objects.get(id = Item_id)})
    #'username': auth.get_user(request).username

def add(request):
    cart_id = request.COOKIES.get("cart")
    item_id = request.GET.get('item', '')[5:]
    res = HttpResponse("Added")
    try:
        cart = Cart.objects.filter(id = cart_id)[0]
    except:
        cart = Cart()
        cart.save()
        res.set_cookie("cart", cart.id)
    try:
        item = Item.objects.filter(id = item_id)[0]
        cart.items.add(item)
        cart.save()
    except:
        pass
    return res

def delete(request):
    cart_id = request.COOKIES.get("cart")
    item_id = request.GET.get('item', '')[5:]
    res = HttpResponse("Added")
    try:
        cart = Cart.objects.filter(id = cart_id)[0]
    except:
        cart = Cart()
        cart.save()
        res.set_cookie("cart", cart.id)
    try:
        item = Item.objects.filter(id = item_id)[0]
        cart.items.remove(item)
        cart.save()
    except:
        pass
    return res

def mycart(request):
    ps = get_template('polls/mybasket.html')

    cart_id = request.COOKIES.get("cart")
    try:
        cart = Cart.objects.filter(id = cart_id)[0]
    except:
        cart = Cart()
        cart.save()

    html = ps.render({'Cart_items' : cart.items.all()})
    res = HttpResponse(html)
    res.set_cookie("cart", cart.id)
    return res

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

@csrf_exempt
def paypal_success(request):
    """
    Tell user we got the payment.
    """
    return HttpResponse("Money is mine. Thanks.")


def paypal_pay(request):
    """
    Page where we ask user to pay with paypal.
    """
    cart_id = request.COOKIES.get("cart")
    try:
        cart = Cart.objects.filter(id = cart_id)[0]
    except:
        cart = Cart()
        cart.save()
    price = 0
    for item in cart.items.all():
        price += item.price

    paypal_dict = {
        "business": "b2239543-facilitator@gmail.com",
        "amount": str(price) + ".00",
        "currency_code": "RUB",
        "item_name": "things",
        "invoice": cart_id,
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