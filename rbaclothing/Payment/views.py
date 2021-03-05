from django.shortcuts import render

# Create your views here.
from django.contrib import messages
from django.shortcuts import render,redirect
from .models import Invoice


def invoice(request):
    ship= request.POST["ship"]
    contact= request.POST["contact"]
    amount = request.POST["amount"]
    id = request.POST["id"]

    invoice= Invoice(shipping_address=ship, Amount=amount, Contact=contact, Customer_Id_id=id)
    invoice.Customer_Id= request.user
    invoice.save()
    messages.info(request, "Your product will be delivered with in 3 days")
    return redirect('/')

