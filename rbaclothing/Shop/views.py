from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.shortcuts import redirect
from django.utils import timezone
from .models import Product,OrderItem
from math import ceil
from django.contrib.auth.decorators import login_required
from .decorators import allowed_users

# Create your views here.

def index(request):
    if request.GET:
        query = request.GET.get('q')
        product = get_data_queryset(str(query))  # typeCasting query to sting
    else:
        product = Product.objects.all()

    cart = 0
    if request.user.username:
        cart = OrderItem.objects.filter(Customer_Id_id=request.user.id).count()
    params = { 'product': product, "cart": cart}

    return render(request, 'shop/index.html', params)

def view_product(request, pk):
    if request.method == "POST":
        product = Product.objects.get(pk=pk)
    else:
        product = Product.objects.get(pk=pk)
    params = {'product': product}
    return render(request, 'shop/product.html', params)

@login_required(login_url="/Login/")
def itemdetail(request):
    orderitems = ''
    if request.user.username:
        orderitems = OrderItem.objects.filter(Customer_Id_id=request.user.id).all()

    params = {'orderitems': orderitems}

    return render(request, "Shop/item.html", params)

@login_required(login_url="/Login/")
def add_to_cart(request, id):
    # login user object
    user = request.user
    # checking if data is exists or not
    if OrderItem.objects.filter(Customer_Id_id=user.id, item_id=id, ordered=False).exists():
        # update quantity
        order = OrderItem.objects.filter(Customer_Id_id=user.id, item_id=id).get();
        order.quantity += 1
        order.save()
        messages.info(request, "This item is added to your cart")
    else:
        # insert a data in a row
        OrderItem.objects.create(item_id=id, Customer_Id_id=user.id, ordered=False)

    # return HttpResponse('created')
    return redirect("/")


def remove_from_cart(request, id):
    user = request.user

    if OrderItem.objects.filter(Customer_Id_id=user.id, item_id=id, ordered=False).exists():
        order = OrderItem.objects.filter(Customer_Id_id=user.id, item_id=id).get();
        order.quantity = 0
        order.save()
        if int(order.quantity) == 0:
            order.delete()
        messages.info(request, "This item has been removed from your cart")

    else:
        # OrderItem.objects.create(item_id = id ,Customer_Id_id = user.id,ordered=False)
        messages.info(request, "Item is not in the cart")
    return redirect("/")


def get_data_queryset(query=None):  #Searching #queryset= search garda aaaune
	queryset = []
	queries = query.split(" ")
	for q in queries:
		product = Product.objects.filter(
				       Q(Product_Name__icontains=q) |
				       Q(Product_Category__icontains=q)
			    )
		for product in product:
			queryset.append(product)

	return list(set(queryset))


def increase(request, id):
    item = OrderItem.objects.get(id=id)
    item.quantity += 1
    item.save()

    return redirect("itemdetail")

def decrease(request, id):
    item = OrderItem.objects.get(id=id)
    item.quantity = int(item.quantity) - 1
    item.save()
    if int(item.quantity)==0:
        item.delete()


    return redirect("itemdetail")

@allowed_users(allowed_roles=['customer'])
def Checkout(request):
    orderitems = ''
    total=0
    totalamount=0
    if request.user.username:
        orderitems = OrderItem.objects.filter(Customer_Id_id=request.user.id).all()

    for i in orderitems:
        total =  i.quantity * i.item.Product_Price
        totalamount = totalamount + total

    params = {'totalamount': totalamount}

    return render(request,"Payment/Checkout.html",params)