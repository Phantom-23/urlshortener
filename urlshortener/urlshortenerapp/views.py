from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Long

# Create your views here.
def hello_world(request):
    return HttpResponse("HELLO how are you!!*_'")

def task_t(request):
    context={"year":"2022","attendees":["rahul","abhi","amu"]}
    return render(request,"task.html",context)    

def home_page(request) :
    context={
        "submitted":False,
        "error":False
    }
    if request.method=="POST":
        #print(request.POST)
        data=request.POST
        longurl=data['longurl']
        customname=data['custom_name']
        try:
            context["longurl"]=longurl
            context["custom_name"]=request.build_absolute_uri()+customname
            customname=request.build_absolute_uri()+customname
            obj=Long(longurl=longurl,custom_name=customname)
            obj.save()
            context["submitted"]=True
            context["date"]=obj.created_date
            context["clicks"]=obj.visit_count
        except :
            context["error"]=True   

    else :
        print("USER didn't entered data")
 
    return render(request,"index.html",context)    

def redirect_url(request,customname):
    #return HttpResponse(customname)
    row=Long.objects.filter(custom_name=customname)
    if len(row)==0:
        return HttpResponse("Error 404 This endpoint doesn't exist")  
    obj=row[0]
    lon_url=obj.longurl    
    obj.visit_count+=1
    obj.save()
    return redirect(lon_url)
    """
def redirect_url(request,customname):
    row=Long.objects.filter(custom_name=customname)
    print(row)
    if len(row)==0:
        return HttpResponse("This endpoint dosen't exist Error!!")
    obj=row[0]
    lonurl=obj.longurl
    obj.visit_count+=1
    obj.save()
    return redirect(lonurl)    
    """
    
def analytics(request):
    rows=Long.objects.all()
    context={
        "rows":rows
    }
    return render(request,"analytics.html",context)