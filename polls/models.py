from __future__ import unicode_literals

from django.db import models

class Category(models.Model):
	name = models.CharField(max_length=200)

class Item(models.Model):
    name = models.CharField(max_length = 200)
    price = models.IntegerField(default = 0)
    photo = models.ImageField(default = None)
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return self.name

class Comments(models.Model):
	class Meta:
		db_table = "comments"
	comment_text = models.TextField()
	comments_Item = models.ForeignKey(Item)

class Cart(models.Model):
	items = models.ManyToManyField(Item)

# Create your models here.
