from django.urls import path
from .views import invoice_list, invoice_detail, invoice_detail_list, invoice_detail_item, index


urlpatterns = [
    path('', index),
    path('invoices/', invoice_list),   #This URL will be used to list all invoices and create a new invoice.
    path('invoices/<int:pk>/', invoice_detail),  #This URL will be used to retrieve, update, or delete a specific invoice by its primary key (pk).
    path('invoice-details/', invoice_detail_list),  #This URL will be used to list all invoice details and create a new invoice detail.
    path('invoice-details/<int:pk>/', invoice_detail_item),  #This URL will be used to retrieve, update, or delete a specific invoice detail by its primary key (pk).
]
