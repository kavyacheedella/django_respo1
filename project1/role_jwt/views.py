from django.shortcuts import render
from django.http import JsonResponse
from .models import RoleDetails
from django.contrib.auth.hashers import make_password,check_password
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime,timedelta
import jwt,json
from django.conf import settings
# Create your views here.

@csrf_exempt
def signup_view(request):
    try:
        if request.method == "POST":
            data = json.loads(request.body)

            username = data.get("username")
            email = data.get("email")
            password = data.get("password")
            role = data.get("role")

            if RoleDetails.objects.filter(username = username).exists():
                return JsonResponse({"error":"username already exists"},status = 400)
            if RoleDetails.objects.filter(email=email).exists():
                return JsonResponse({"error":"email already exists"},status = 400)
            
            RoleDetails.objects.create(
                username = username,
                email = email,
                password = make_password(password),
                role = role
            )

            return JsonResponse({"status":"success","msg":"user successfully signed"},status = 200)
        return JsonResponse({"status":"error","msg":"only post method is allowed"},status = 400)
    except Exception as e:
        return JsonResponse({"status":"error" , "msg":str(e)},status = 400) 
    
@csrf_exempt
def login_view(request):
    try:
        if request.method == "POST":
            data = json.loads(request.body)

            username = data.get("username")
            password = data.get("password")
            role = data.get("role")

            if not username or not password:
                return JsonResponse({"status":"error","msg":"all fields are required"},status = 400)
            
            try:
                user = RoleDetails.objects.get(username = username)
            except RoleDetails.DoesNotExist:
                return JsonResponse({"status":"error","msg":"invalid credentials"},status = 400)
            
            if not check_password(password,user.password):
                return JsonResponse({"status":"error","msg":"invalid password"},status = 400)
            
            request.session["user_id"] = user.id
            request.session["username"] = user.username

            payload = {
                "user_id":user.id,
                "username":user.username,
                "role":user.role,
                "exp":datetime.utcnow() + timedelta(minutes=30)
            }

            token = jwt.encode(
                payload,
                settings.SECRET_KEY,
                algorithm="HS256"
            )
            return JsonResponse({"access_token": token},status=200)
        return JsonResponse({"status":"error" , "msg":"only post method is allowed"},status = 400)
    except Exception as e:
        return JsonResponse({"status":"error","msg":str(e)},status = 400)
    
@csrf_exempt  
def protected_view(request):

    auth_header = request.headers.get("Authorization")

    if not auth_header or not auth_header.startswith("Bearer "):
        return JsonResponse(
            {"error": "Authorization header missing"},
            status=401
        )

    token = auth_header.split(" ")[1]

    try:
        payload = jwt.decode(
            token,
            settings.SECRET_KEY,
            algorithms=["HS256"]
        )

        return JsonResponse({
            "message": "Access granted",
            "user_id": payload.get("user_id"),
            "username": payload.get("username"),
            "role": payload.get("role")
        })

    except jwt.ExpiredSignatureError:
        return JsonResponse({"error": "Token expired"}, status=401)

    except jwt.InvalidTokenError:
        return JsonResponse({"error": "Invalid token"}, status=401)

    
@csrf_exempt
def admin_only_view(request):
    auth_header = request.headers.get("Authorization")

    token = auth_header.split(" ")[1]
    payload = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])

    if payload["role"] != "admin":
        return JsonResponse({"error": "Forbidden"}, status=403)

    return JsonResponse({"message": "Welcome Admin"})
