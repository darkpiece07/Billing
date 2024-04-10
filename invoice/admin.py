from django.contrib import admin
from .models import Invoice, InvoiceDetail

# Register your models here.

class InvoiceAdmin(admin.ModelAdmin):
    list_display = ['date', 'customer_name']

class InvoiceDetailAdmin(admin.ModelAdmin):
    list_display = ['description', 'quantity', 'unit_price', 'price']


admin.site.register(Invoice, InvoiceAdmin)
admin.site.register(InvoiceDetail, InvoiceDetailAdmin)