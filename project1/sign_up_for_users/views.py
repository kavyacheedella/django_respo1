from django.shortcuts import render
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import user_login
# Create your views here.
@csrf_exempt
def user_profile(request):

    if request.method != "POST":
        return JsonResponse(
            {"error": "Only POST method is allowed"},
            status=405
        )

    try:
        data = json.loads(request.body)
    except json.JSONDecodeError:
        return JsonResponse(
            {"error": "Invalid JSON"},
            status=400
        )

    username = data.get("username")
    email = data.get("email")
    password = data.get("password")

    if not username or not email or not password:
        return JsonResponse({"error": "All fields are required"},status=400)

    if user_login.objects.filter(username=username).exists():
        return JsonResponse({"error": "username already exists"},status=409)

    if user_login.objects.filter(email=email).exists():
        return JsonResponse({"error": "email already exists"},status=409)

    user_login.objects.create(
        username=username,
        email=email,
        password=password
    )

    return JsonResponse(
        {"message": "details entered successfully"},
        status=201
    )
