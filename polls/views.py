from django.http import HttpResponse
from polls.models import Item
from django.template.loader import get_template 
from django.shortcuts import render_to_response
from django.template import Context

def catalog(request):
    ps = get_template('polls/catalog.html')
    html = ps.render({'Items' : Item.objects.all()}) 
    return HttpResponse(html)


def index(request):
    html = "aaa"

    return HttpResponse(html)

def item(request, Item_id = 1):
    return render_to_response('polls/item.html', {'Item' : Item.objects.get(id = Item_id)})

def item1(request):
    #ps = get_template('polls/item.html')
    print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
    print(request)
    print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
    #html = ps.render({'Item' : Item.objects.}) &&&

    ps = get_template('polls/catalog.html')
    html = ps.render({'Items' : Item.objects.all()}) 
    return HttpResponse(html)

def mycart(request):
    ps = get_template('polls/mycart.html')
    html = ps.render()
    return HttpResponse(html)


pass