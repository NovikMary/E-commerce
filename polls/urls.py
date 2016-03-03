from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^catalog[//]?$', 'polls.views.catalog'),
    url(r'^cart\?*', 'polls.views.mycart'),
    url(r'^item_(?P<Item_id>\d+)$', 'polls.views.item'),
    #    url(r'^3/', 'polls.views.templates_3_easy'),
]