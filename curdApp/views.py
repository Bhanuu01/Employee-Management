from django.shortcuts import render,redirect
from .models import ClientInfo

# Create your views here.

def home(request):
    all_clients = ClientInfo.objects.all()
    return render(request,'index.html',{'context': all_clients})

def add_client(request):
    if request.method == 'POST':
        print('post')
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        phone = request.POST.get('phone')

        client = ClientInfo(name=name,email=email,address=address,phone=phone)
        client.save()
        print('saved in database')
        
        return redirect('home')
    return render(request,'index.html')

def delete_client(request,id):
    client = ClientInfo.objects.get(id=id)
    client.delete()
    all_clients = ClientInfo.objects.all()
    for i in all_clients:
        print(i.email)
    return redirect('home')

def edit_client(request,id):
    print('print(request.POST.get)')
    if request.method == 'POST':
        print(request.POST.get)
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
         
        client = ClientInfo.objects.get(id=id)

        client.name = name
        client.email = email
        client.address = address
        client.phone = phone
        client.save()

        return redirect('home')
    else:
        client = ClientInfo.objects.get(id=id)
        context = {
            'client': client,
        }
        return render(request,'edit.html',context)


    
