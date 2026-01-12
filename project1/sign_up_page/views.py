from django.shortcuts import render
import json
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from .models import StudentProfile
# Create your views here.

@csrf_exempt

def signup(request):
    try:
        if request.path == "/signup" and request.method == 'POST':
            data = json.loads(request.body)

            user = User.objects.create_user(
                username=data.get("username"),
                email=data.get("email"),
                password=data.get("password")
            )
            StudentProfile.objects.create(user=user)
            return JsonResponse({"message": "Signup successful"},status=201)
        else:
            return JsonResponse({"error":"only post method is allowed"},status = 405)
    
    except Exception as e:
        return JsonResponse({"status":"error" , "message":str(e)},status = 400)
