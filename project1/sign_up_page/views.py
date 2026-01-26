from django.shortcuts import render
import json
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt
from .models import StudentProfile
# Create your views here.

@csrf_exempt

def signup_view(request):
    try:
        if request.method == 'POST':
            data = json.loads(request.body)

            user = User.objects.create_user(
                username=data.get("username"),
                email=data.get("email"),
                password=data.get("password")
            )
            return JsonResponse({"message": "Signup successful"},status=201)
        else:
            return JsonResponse({"error":"only post method is allowed"},status = 405)
    
    except Exception as e:
        return JsonResponse({"status":"error" , "message":str(e)},status = 400)
    
@csrf_exempt
def login_view(request):
    if request.method != "POST":
        return JsonResponse({"error": "POST method only"}, status=405)

    try:
        data = json.loads(request.body)
    except Exception:
        return JsonResponse({"error": "Invalid JSON"}, status=400)

    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return JsonResponse(
            {"error": "Username and password required"},
            status=400
        )

    # 🔑 AUTHENTICATION
    user = authenticate(username=username, password=password)

    if user is None:
        return JsonResponse(
            {"error": "Invalid credentials"},
            status=401
        )

    # 🧠 BUILT-IN SESSION CREATION
    login(request, user)

    return JsonResponse(
        {"status": "success", "msg": "Login successful"},
        status=200
    )

@csrf_exempt
def logout_view(request):
    if request.method != "POST":
        return JsonResponse({"error": "POST method only"}, status=405)

    logout(request)

    return JsonResponse(
        {"status": "success", "msg": "Logged out successfully"},
        status=200
    )




