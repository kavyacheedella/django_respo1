from django.shortcuts import render
import json
from django.http import JsonResponse
from django.contrib.auth.hashers import make_password,check_password
from django.views.decorators.csrf import csrf_exempt
from .models import AppUser
# Create your views here.
@csrf_exempt

def signup(request):
    if request.method != "POST":
        return JsonResponse({"error": "POST only"}, status=405)

    data = json.loads(request.body)

    username = data.get("username")
    email = data.get("email")
    password = data.get("password")

    if AppUser.objects.filter(username=username).exists():
        return JsonResponse({"error": "Username exists"}, status=409)

    if AppUser.objects.filter(email=data["email"]).exists():
        return JsonResponse({"error": "Email exists"}, status=409)

    AppUser.objects.create(
        username=username,
        email=email,
        password=make_password(password)
    )

    return JsonResponse({"status": "success", "msg": "Registered"}, status=201)
  

@csrf_exempt
def login(request):
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
            {"error": "Username and password are required"},
            status=400
        )

    try:
        user = AppUser.objects.get(username=username)
    except AppUser.DoesNotExist:
        return JsonResponse(
            {"error": "Invalid credentials"},
            status=401
        )

    # 🔐 SECURE PASSWORD CHECK
    if not check_password(password, user.password):
        return JsonResponse(
            {"error": "Invalid credentials"},
            status=401
        )

    # 🧠 SESSION CREATION
    request.session["user_id"] = user.id
    request.session["username"] = user.username

    return JsonResponse(
        {"status": "success", "msg": "Login successful"},
        status=200
    )
  




