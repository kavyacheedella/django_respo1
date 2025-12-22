from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
import math
import json
from django.views.decorators.csrf import csrf_exempt
from basic1.models import userProfile,employeeProfile
# Create your views here.
def home(request):
    return render(request,'home.html')
def services(request):
    return render(request,'services.html')
def contact(request):
    return render(request,'contact.html')
def index(request):
    return render(request,'index.html')

def sample(request):
    print(request)
    qp1 = request.GET.get("name")
    qp2=request.GET.get("city")
    return HttpResponse(f"{qp1} is from {qp2}")

def sample1(request):
    data = {
        'name':'kavya',
        'age':22,
        'place':'kerala'
    }
    return JsonResponse(data)

def sample2(request):
    data = ['kavya','anu','senha']
    return JsonResponse(data,safe=False)

@csrf_exempt
def createData(request):
    if request.method == "POST":
        data = json.loads(request.body)
        print(data)
    return JsonResponse({"status":"success"})

@csrf_exempt
def createProduct(request):
    # data = {}
    if request.method == "POST":
        data=json.loads(request.body)
        print(data)
        return JsonResponse({"status":"success","data":data,"status code":201})
    return JsonResponse({
        "status": "error",
        "message": "Only POST method allowed"
    }, status=405)
    
@csrf_exempt
def userdata(request):
    try:
        if request.method == "POST":
            data = json.loads(request.body)
            name = data.get("name")
            city = data.get("city")
            age = data.get("age")
            userProfile.objects.create(name = name,city = city,age = age)
            print(data)
        return JsonResponse({"status":"success","data":data,"statuscode":201},status=201)
    except Exception as e:
        return JsonResponse({"status":"error","message":str(e)}, status=400)

@csrf_exempt
def employee_data(request):
    try:
        if request.method == "POST":
            data = json.loads(request.body)
            emp_name = data.get("emp_name")
            emp_salary = data.get("emp_salary")
            emp_email = data.get("emp_email")

            employeeProfile.objects.create(
                emp_name = emp_name , 
                emp_salary = emp_salary , 
                emp_email = emp_email
                )
            
            print(data)
        return JsonResponse({"status":"success","data":data,"statuscode":201},status=201)
    except Exception as e:
        return JsonResponse({"status":"error","message":str(e)}, status=400)




