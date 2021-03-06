"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
import social.apps.django_app.urls
import polls.views
import paypal.standard.ipn.urls


urlpatterns = [
    url(r'^$', polls.views.redirect_catalog),
    url(r'^item_(?P<Item_id>\d+)$', polls.views.item),
    url(r'^page/item_(?P<Item_id>\d+)$', polls.views.item),
    url(r'^admin/', admin.site.urls),
    url(r'^cart/*', polls.views.mycart),
    url(r'^page/(\d+)$', polls.views.catalog),
    url(r'^page/(\d+)/category/(\d+)$', polls.views.catalog),
    url(r'^add-to-cart/$', polls.views.add),
    url(r'^delete-from-cart/$', polls.views.delete),

    url(r'^static/(?P<path>.*)$', 'django.views.static.serve',
		{'document_root', settings.STATIC_ROOT}
	),
    url('', include(social.apps.django_app.urls, namespace='social')),
    url(r'^accounts/logout/$', polls.views.account_logout, name='logout'),
    url(r'^accounts/login/$', polls.views.home, name='login'),
    url(r'^accounts/profile/$', polls.views.account_profile, name='profile'),

    url(r'^paypal/', include(paypal.standard.ipn.urls)),
    url(r'^payment/cart/$', polls.views.paypal_pay, name='cart'),
    url(r'^payment/success/$', polls.views.paypal_success, name='success'),

]  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
