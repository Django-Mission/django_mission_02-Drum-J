from django.contrib import admin
from .models import FAQ
# Register your models here.
@admin.register(FAQ)
class FAQModelAdmin(admin.ModelAdmin) :
    list_display = ('qus','category','ans','writer','created_at','writer2','modify_date')