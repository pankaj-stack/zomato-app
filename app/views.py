from django.shortcuts import render, redirect
from .models import CustomerRegisteration, Hotels, Menu
from django.contrib.auth.hashers import make_password, check_password

# Create your views here.
d={}
def hotel_view(request):
    if request.method == 'POST':
        return redirect('http://localhost:8000/menu_item/')
    else:
        hotels=Hotels.objects.all()
        return render(request,'hotel_image.html',{'hotels':hotels})

def menu_view(request):
    if request.method == 'POST':
        return redirect('http://localhost:8000/login/')
    menu = Menu.objects.all()
    return render(request,'menu.html',{'menu':menu})

def register_view(request):
    if request.method == 'POST': #Here post  means when you press the submit button of the forms
        if CustomerRegisteration.objects.filter(email_id = request.POST['emailid']).exists():
            return render(request,'register.html',{'error_message':'Customer is already registered'})
        else:
            customer =CustomerRegisteration()
            customer.first_name = request.POST['firstname'] #firstname is assigned into first_name of database column
            customer.last_name = request.POST['lastname']
            customer.email_id = request.POST['emailid']
            customer.password = make_password(request.POST['password']) #make_password takes the noramal pasword and then it apply on it  hashing
            customer.phone_no = request.POST['phonenumber']
            customer.address = request.POST['address']
            customer.save() #to save the fronend user data into database
            return redirect('http://localhost:8000/login/')
    else:
        return render(request,'register.html')

def login_view(request):
    if request.method == 'POST':
        if CustomerRegisteration.objects.filter(email_id = request.POST['emailid']).exists():
            customer=CustomerRegisteration.objects.get(email_id = request.POST['emailid'])
            if check_password(request.POST['password'],customer.password):
                return redirect('http://localhost:8000/thank_you/')
            else:
                return render(request,'login.html',{'error_message':'Incorrect password'})
        else:
            return render(request,'login.html',{'error_message':'Incorrect email-id'})

    else:
        return render(request,'login.html')



def registeration_view(request):
    data_list = RegisterationForm.objects.all()
    return render(request,'registeration_form.html',{'data_list':data_list})

def thank_you_page(request):
    return render(request,'thanku_page.html')