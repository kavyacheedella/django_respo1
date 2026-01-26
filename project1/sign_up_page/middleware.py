from django.http import JsonResponse
import re
import json

class regexMiddleware:
    def __init__(self,get_response):
        self.get_response = get_response

        self.username_pattern = re.compile(r'^[a-zA-Z0-9_]{4,20}$')
        self.email_pattern = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
        self.password_pattern = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$')

    def __call__(self, request):

        if request.path in ["/signup" , "/login"] or request.method == "POST":
            
            try:
                data = json.loads(request.body)
            except Exception as e:
                return JsonResponse({"error":"Invalid JSON"},status = 403)
            
            if request.method == "/signup":
                
                username = data.get("username", "") 
                email = data.get("email", "") 
                password = data.get("password", "").strip() 

                if not username or not email or not password:
                    return JsonResponse({"error": "All fields are required"}, status=400)
                if not self.username_pattern.fullmatch(username): 
                    return JsonResponse({ "error" :"Invalid username format" }, status = 400) 
                if not self.email_pattern.fullmatch(email): 
                    return JsonResponse({ "error" :"invalid email format" }, status = 400) 
                if not self.password_pattern.fullmatch(password): 
                    return JsonResponse({ "error" :"invalid password format" },status = 400)
                
            if request.method == "/login":

                username = data.get("username")
                password = data.get("password")

                if not username or not password:
                    return JsonResponse({"error":"username and password are invalid"},status = 400) 
        
        response = self.get_response(request)
        return response




