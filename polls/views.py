from django.http import HttpResponse
from polls.models import Item
from django.template.loader import get_template 
from django.shortcuts import render_to_response
from django.template import Context
from django.core.paginator import Paginator
from django.contrib.auth import logout

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


pass