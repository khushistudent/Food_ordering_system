from django.shortcuts import render,redirect,HttpResponse
from .models import *

# Create your views here.
def home(request):
    return render(request,"user/home.html")
def Register(request):
    if request.method=="POST":
         Name=request.POST.get("name")
         mobile=request.POST.get("mobile")
         email=request.POST.get("email")
         password=request.POST.get("password")
         Image=request.FILES["fu"]
         Address=request.POST.get("address")
         formdata=tblregister.objects.all().filter(Email=email).count()
         if formdata==0:
              tblregister(Full_Name=Name,mobile= mobile,Email=email,Password=password,Image=Image,Address=Address).save()
              return HttpResponse("<script> alert('You are registered..'); location.href='/register/'</script>")
         else:
              return HttpResponse("<script> alert('You are already register..'); location.href='/register/'</script>")
    return render(request,"user/Register.html")
def about(request):
    return render(request,"user/about.html")

def login(request):
     
     if request.method == "POST":
          Email=request.POST.get("email")
          password=request.POST.get("pass")
          formdata=tblregister.objects.all().filter(Email=Email,Password=password).count()
          if formdata==1:
              tbllogin.objects.create(Email=Email,password=password)
              return HttpResponse("<script>alert('You are login successfully');location.href='/menu/'</script>")
          else:
               return HttpResponse("<script>alert('Your email or password lis incorrect. Please register first...');location.href='/login/'</script>")
            #    return render(request,'user/login.html',{"msg":"Your Email or Password is incorrect.."})
     return render(request,"user/login.html")


def menu(request):
    data=tblgallery.objects.all()
    for x in data:
       x.star_range = range(x.rating)
    mydict={'gdata':data}
    return render(request,"user/menu.html",mydict)
def review(request):
    if request.method == "POST":
               Name=request.POST.get("name")
               
              
               Feedback=request.POST.get("msg")
              
               image=request.FILES.get("Image")
               tblreview(Full_Name= Name,Feedback= Feedback,Image=image).save()
    reviews=tblreview.objects.all().order_by('-id')#databse me save sare feedback ko nikal kar reviews naam ke variable me store kar rhi hai
    return render(request,"user/review.html",{'reviews':reviews})


def reservation(request):
    
    if request.method == "POST":
        full_name=request.POST.get("name")
        Phone=request.POST.get("phone")
        email=request.POST.get("email")
        date=request.POST.get("date")

        Guests=request.POST.get("guest")
        Time=request.POST.get("time")
        Special_Request=request.POST.get("message")
        # mydict={"full_name":full_name,"Phone":Phone,"email":email,"date":date,"Guests":Guests,"Time":Time," Special_Request": Special_Request}
        tblreservation(Full_Name= full_name,Phone=Phone,email=email,date=date,guests=Guests,time=Time,special_requests=  Special_Request).save()
        
    return render(request,"user/reservation.html",)
def contact(request):
   
    if request.method == "POST":
           Name=request.POST.get("Name")
           Phone=request.POST.get("Phone")
           email=request.POST.get("Email")
           Message=request.POST.get("Message")
           tblContact(Full_Name= Name,Phone=Phone,email=email,Message=Message).save()
           
    return render(request,"user/contact.html")