from django.contrib import admin
from .models import StoreItem, StoreItemReview

# Register your models here.
admin.site.register(StoreItem)
admin.site.register(StoreItemReview)