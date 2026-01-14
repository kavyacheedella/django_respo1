from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import UserProfile

@csrf_exempt
def user_data(request):
    try:
        if request.method == "POST":
            data = json.loads(request.body)

            # Read data from request JSON
            user_name = data.get("name")
            user_email = data.get("email")
            user_age = data.get("age")
            user_city = data.get("city")

            # Required field validation
            if not user_name or not user_email or not user_age or not user_city:
                return JsonResponse(
                    {"error": "All fields (name, email, age, city) are required"},
                    status=400
                )

            # Duplicate checks (MODEL FIELD NAMES)
            if UserProfile.objects.filter(name=user_name).exists():
                return JsonResponse(
                    {"error": "name already exists"},
                    status=400
                )

            if UserProfile.objects.filter(email=user_email).exists():
                return JsonResponse(
                    {"error": "email already exists"},
                    status=400
                )

            # Age validation
            if not str(user_age).isdigit():
                return JsonResponse(
                    {"error": "Age must be numeric"},
                    status=400
                )

            if int(user_age) < 18:
                return JsonResponse(
                    {"error": "Age must be 18 or above"},
                    status=400
                )

            # Create record (USE MODEL FIELD NAMES)
            UserProfile.objects.create(
                name=user_name,
                email=user_email,
                age=int(user_age),
                city=user_city
            )

            return JsonResponse(
                {"status": "success", "message": "Details entered successfully"},
                status=201
            )

        return JsonResponse(
            {"error": "Only POST method is allowed"},
            status=405
        )

    except Exception as e:
        return JsonResponse(
            {"status": "error", "message": str(e)},
            status=400
        )



    #Latest to oldest
    # sort_by = UserProfile.objects.order_by('-created_at')
    #oldest to latest
    # sort_by = UserProfile.objects.order_by('created_at')
    #limit users
    # UserProfile.objects.order_by('-created_at')[:5]

def get_users(request):

    try:
        if request.method == "GET":

            # Read query parameters
            city = request.GET.get("city")
            min_age = request.GET.get("min_age")

            users = UserProfile.objects.all()
            # users = UserProfile.objects.all().order_by('-created_by')
            
            # Apply city filter if provided
            if city:
                users = users.filter(city__iexact=city)

            # Apply minimum age filter if provided
            if min_age and min_age.isdigit():
                users = users.filter(age__gte=int(min_age))

            users = users.order_by('-created_at')

            data = [
                {
                    "name": user.name,
                    "email": user.email,
                    "age": user.age,
                    "city": user.city,
                    "created_at": user.created_at
                }
                     for user in users
                    ]
            return JsonResponse({"status": "success","count": len(data),"users": data},safe=False)
        
        return JsonResponse({"error":"only get method is allowed"},status = 403)
    
    except Exception as e:
        return JsonResponse({"status":"error" , "message" : str(e)},status=405)

