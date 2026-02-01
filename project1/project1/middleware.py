import re,json
from django.http import JsonResponse

class Checkingmiddleware:

    def __init__(self , get_response):
        self.get_response = get_response

        self.username_regex = re.compile(r'^[A-Za-z0-9._]{4,20}$')
        self.email_regex = re.compile(r'^[a-zA-Z0-9.+%_-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
        self.password_regex = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*/d)(?=.*[@$!%*?&])[a-zA-Z\d@$!%*?&]{8,}$')

    def __call__(self,request):

        JSON_REQUIRED_PATHS = ["/login/", "/signup/"]

        if request.path in JSON_REQUIRED_PATHS:
            if request.method == "POST":

                if not request.body:
                    return JsonResponse({"error": "Request body required"},status=400)
                try:
                    data = json.loads(request.body)
                except json.JSONDecodeError:
                    return JsonResponse({"error": "Invalid JSON format"},status=400)
            
            if request.method == "/signup":

                username = data.get("username")
                email = data.get("email")
                password = data.get("password")

                if not username or not email or not password:
                    return JsonResponse({"error":"All fields are required"},status = 400)
                if self.username_regex.fullmatch(username):
                    return JsonResponse({"error":"invalid username format"},status = 400)
                if self.email_regex.fullmatch("email"):
                    return JsonResponse({"error":"invalid email format"},status = 400)
                if self.password_regex.fullmatch("password"):
                    return JsonResponse({"error":"invalid password format"},status = 400)
                
            if request.method == "/login":

                username = data.get("username")
                password = data.get("password")

                if not username or not password:
                    return JsonResponse({"error":"username and password are invalid"},status = 400) 
                
        return self.get_response(request)

        
