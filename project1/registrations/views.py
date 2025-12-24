from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from registrations.models import CourseRegistration
# Create your views here.
@csrf_exempt
def student_registration(request):
    try:
        if(request.method=='POST'):
            data = json.loads(request.body)
            details = CourseRegistration.objects.create(
                name = data.get("student_name"),
                email = data.get("student_mail"),
                course = data.get("student_course"),
                phone = data.get("student_phnum"),
                registered_at = data.get("register_time")
            )
            return JsonResponse({"status":"registration success","data":data},status = 201)
        else:
            return JsonResponse({"status":"only post method is allowed"},status = 400)
    except Exception as e:
        return JsonResponse({"status":"registration failed","error":str(e)},status = 500)

def get_student_details(request):
    student_details = CourseRegistration.objects.values()
    total_record = CourseRegistration.objects.count()
    data = []
    for student in student_details:
        data.append(
            {
             "student_name":student.get("name"),
             "student_mail":student.get("email"),
             "student_course":student.get("course"),
             "student_phnnum":student.get("phone"),
             "register_time":student.get("registered_at")
            }
        )
        return JsonResponse({"status":"data fetch successfully","data":data,"total":total_record})