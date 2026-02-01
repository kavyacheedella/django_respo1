from django.shortcuts import render
import json
from django.http import JsonResponse
from .models import details
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime, timedelta
import jwt
from django.conf import settings
# Create your views here.

@csrf_exempt
def signup_view(request):
    try:
        if request.method == "POST":
            data = json.loads(request.body)


            user = User.objects.create_user(   
                username = data.get("username"),
                email = data.get("email"),
                password = data.get("password")
            )
             
            #  to get details in our model also we create orm for our own model
            details.objects.create(
                username = data.get("username"),
                email = data.get("email"),
                password = data.get("password")
            )

            return JsonResponse({"status":"signup successfull"},status = 201)
        return JsonResponse({"status":"error","msg":"only post method is allowed"},status = 400)

    except Exception as e:
        return JsonResponse({"status":"error", "msg":str(e)},status = 400)



@csrf_exempt
def login_view(request):
    try:
        if request.method != "POST":
            return JsonResponse(
                {"error": "Only POST method is allowed"},
                status=405
            )

        data = json.loads(request.body)

        username = data.get("username")
        password = data.get("password")

        if not username or not password:
            return JsonResponse(
                {"error": "Username and password are required"},
                status=400
            )

        # 🔐 AUTHENTICATE USER
        user = authenticate(username=username, password=password)

        if not user:
            return JsonResponse(
                {"error": "Invalid credentials"},
                status=401
            )

        # 🧾 JWT PAYLOAD
        payload = {
            "user_id": user.id,
            "username": user.username,
            "exp": datetime.utcnow() + timedelta(minutes=30)
        }

        # 🔑 CREATE TOKEN
        token = jwt.encode(
            payload,
            settings.SECRET_KEY,
            algorithm="HS256"
        )

        return JsonResponse({"access_token": token},status=200)
    except Exception as e:
        return JsonResponse({"status": "error", "msg": str(e)},status=400)


@csrf_exempt
def protected_view(request):
    try:
        auth_header = request.headers.get("Authorization")

        if not auth_header or not auth_header.startswith("Bearer "):
            return JsonResponse(
                {"error": "Authorization header missing"},
                status=401
            )

        token = auth_header.split(" ")[1]

        payload = jwt.decode(
            token,
            settings.SECRET_KEY,
            algorithms=["HS256"]
        )

        return JsonResponse({
            "message": "Access granted",
            "user_id": payload["user_id"],
            "username": payload["username"]
        })

    except jwt.ExpiredSignatureError:
        return JsonResponse({"error": "Token expired"}, status=401)

    except jwt.InvalidTokenError:
        return JsonResponse({"error": "Invalid token"}, status=401)



