from django.shortcuts import render,HttpResponse
from datetime import datetime
from home1.models import Contact
from django.contrib import messages
# Create your views here.

def index(request):
    context={
        'variable':"hello this is sent"
    }
    return render(request,'test.html',context)#passing variables as a context

    # return render(request,'test.html')#showing templet

def link(request):
    # return HttpResponse("This is link page")    
     return render(request,'Link.html')

def contact(request):
    # return HttpResponse("This is contact page")  
    if request.method=="POST":
        email=request.POST.get('email')
        name=request.POST.get('name')
        desc=request.POST.get('desc')
        contact=Contact(email=email,name=name,desc=desc,date=datetime.today())
        contact.save()
        messages.success(request, 'Thank you information saved successfully.....!')
    
    return render(request,'contact.html')

def moongdaal(request):
    # return HttpResponse("This is contact page")  
      return render(request,'moongdaal.html')      

def dhokla(request):
    # return HttpResponse("This is contact page")  
      return render(request,'dhokla.html')    

def about(request):
    # return HttpResponse("This is contact page")  
      return render(request,'about.html')        


def garlicbread(request):
    # return HttpResponse("This is contact page")  
      return render(request,'garlicbread.html')      


def pizzab(request):
    # return HttpResponse("This is contact page")  
      return render(request,'pizzab.html')   

def momos(request):
    # return HttpResponse("This is contact page")  
      return render(request,'momos.html')   

  
def medu(request):
    # return HttpResponse("This is contact page")  
      return render(request,'medu.html') 