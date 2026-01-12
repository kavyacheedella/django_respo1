from django.http import JsonResponse
import json,re


class validationMiddleware:
    def __init__(self,get_response):
        self.get_response = get_response

        self.username_regex = re.compile(r'^[a-zA-Z0-9._]{4,20}$')
        self.email_regex = re.compile(r'^[a-zA-Z0-9_.%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
        self.password_regex = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$')

    def __call__(self, request):
        if request.path == "/signup/" and request.method == "POST":
            try:
                data = json.loads(request.body)
            except Exception as e:
                return JsonResponse({"error":"invalid json"},status = 403)
            
            username = data.get("username","")
            email = data.get("email","")
            password = data.get("password","").strip()

            if not self.username_regex.fullmatch(username):
                return JsonResponse({"error":"invalid username"},status = 403)
            if not self.email_regex.fullmatch(email):
                return JsonResponse({"error":"invalid email format"},status=403)
            if not self.password_regex.fullmatch(password):
                return JsonResponse({"error":"invalid password format"},status=403)
        return self.get_response(request)

