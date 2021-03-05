from django.contrib import messages
from django.shortcuts import render,redirect
from .models import FeedBack
from .decorators import allowed_users

# Create your views here.

@allowed_users(allowed_roles=['customer'])
def Feedback(request):
    if request.method == 'GET':
        image = FeedBack.objects.all()

    return render(request,"Feedback/Feedback.html",{'image': image})

def feedback(request):
    Name= request.POST["Name"]
    Email= request.POST["Email"]
    Subject = request.POST["Subject"]
    Message = request.POST["Message"]
    img = request.FILES.get("image",None)


    feedback= FeedBack(Name=Name, Email=Email, Subject=Subject, Message=Message,img=img)
    feedback.save()
    messages.info(request, "Feed back recorded")
    return redirect('/Feedback/')