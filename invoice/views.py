from django.shortcuts import render, HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Invoice, InvoiceDetail


def index(request):
    return HttpResponse("This is index page!")


@api_view(['GET', 'POST'])
def invoice_list(request):
    if request.method == 'GET':
        invoices = Invoice.objects.all()
        data = [{'id': invoice.id, 'date': invoice.date, 'customer_name': invoice.customer_name} for invoice in invoices]
        return Response(data)

    elif request.method == 'POST':
        invoice_data = request.data
        details_data = invoice_data.pop('details', [])
        invoice = Invoice.objects.create(**invoice_data)
        for detail_data in details_data:
            InvoiceDetail.objects.create(invoice=invoice, **detail_data)
        return Response({'id': invoice.id}, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def invoice_detail(request, pk):
    try:
        invoice = Invoice.objects.get(pk=pk)
    except Invoice.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        data = {
            'id': invoice.id,
            'date': invoice.date,
            'customer_name': invoice.customer_name
        }
        return Response(data)

    elif request.method == 'PUT':
        invoice_data = request.data
        details_data = invoice_data.pop('details', [])
        invoice.date = invoice_data.get('date', invoice.date)
        invoice.customer_name = invoice_data.get('customer_name', invoice.customer_name)
        invoice.save()
        # invoice.details.all().delete()
        for detail_data in details_data:
            InvoiceDetail.objects.create(invoice=invoice, **detail_data)
        return Response(status=status.HTTP_200_OK)

    elif request.method == 'DELETE':
        invoice.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def invoice_detail_list(request):
    if request.method == 'GET':
        invoice_details = InvoiceDetail.objects.all()
        data = [{'id': detail.id, 'invoice_id': detail.invoice_id, 'description': detail.description,
                 'quantity': detail.quantity, 'unit_price': detail.unit_price, 'price': detail.price} for detail in invoice_details]
        return Response(data)

    elif request.method == 'POST':
        detail_data = request.data
        invoice_detail = InvoiceDetail.objects.create(**detail_data)
        return Response({'id': invoice_detail.id}, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def invoice_detail_item(request, pk):
    try:
        invoice_detail = InvoiceDetail.objects.get(pk=pk)
    except InvoiceDetail.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        data = {
            'id': invoice_detail.id,
            'invoice_id': invoice_detail.invoice_id,
            'description': invoice_detail.description,
            'quantity': invoice_detail.quantity,
            'unit_price': invoice_detail.unit_price,
            'price': invoice_detail.price
        }
        return Response(data)

    elif request.method == 'PUT':
        detail_data = request.data
        invoice_detail.description = detail_data.get('description', invoice_detail.description)
        invoice_detail.quantity = detail_data.get('quantity', invoice_detail.quantity)
        invoice_detail.unit_price = detail_data.get('unit_price', invoice_detail.unit_price)
        invoice_detail.price = detail_data.get('price', invoice_detail.price)
        invoice_detail.save()
        return Response(status=status.HTTP_200_OK)

    elif request.method == 'DELETE':
        invoice_detail.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
