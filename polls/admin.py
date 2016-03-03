from django.contrib import admin
from polls.models import Item

# Register your models here.
class ItemAdmin(admin.ModelAdmin):
	fields = ['name', 'price', 'photo']
	list_filter = ['name']

admin.site.register(Item, ItemAdmin)