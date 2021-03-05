from django.shortcuts import render
from .models import Customer
from django.http import HttpResponse, JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView

# Create your views here.

@csrf_exempt
def update_api_data(request, id):
    Cust = Customer.objects.get(id=id)
    if request.method == "GET":
        return JsonResponse({"Name": Cust.Customer_Name,"Gender": Cust.Gender , "DOB": Cust.DateOfBirth})
    
    elif request.method == "PUT":
        decoded_data = request.body.decode('utf-8')
        data = json.loads(decoded_data)
        Cust.Customer_Name = data['Name']
        Cust.save()
        return JsonResponse({"message": "Updated Successfully!!"})

    return HttpResponse("Error")


def Display_API(request):
    if request.method == "GET":
        Cust = Customer.objects.all()
        display= {"Registerd Customer": list(Cust.values("Customer_Name", "Gender","DateOfBirth"))}
        return JsonResponse(display)

    else:
            return HttpResponse("Error")

@csrf_exempt
def Deleta_api_data(request, id):
    if request.method == "DELETE" :
        b = Customer.objects.get(id=id)
        b.delete()
        return JsonResponse({"message":"Deleted Successfully"})

    else:
        return JsonResponse({"message":"Error"})

@csrf_exempt
def postAPI(request):
    if request.method == "POST":
        decoded_data = request.body.decode('utf-8')
        data = json.loads(decoded_data)
        Customer_Name = data["Name"]
        Gender = data["Gender"]
        DateOfBirth = data["DOB"]
        Customer.objects.create(Customer_Name=Customer_Name,Gender=Gender,DateOfBirth=DateOfBirth)
        return JsonResponse({"message":"Customer created"})

    else:
        return HttpResponse("Error")


def pagination(request, PageNo, Size):
    skip = Size*(PageNo-1)
    Cust= Customer.objects.all() [skip:(PageNo * Size)]

    Data={

        "Cust" : list(Cust.values("Customer_Name", "Gender"))

    }

    return JsonResponse(Data)

