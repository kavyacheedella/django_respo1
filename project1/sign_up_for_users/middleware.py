import json, re
from django.http import JsonResponse

class validationMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

        self.username_regex = re.compile(r'^[a-zA-Z0-9._]{4,20}$')
        self.email_regex = re.compile(r'^[\w\.-]+@[\w\.-]+\.\w+$')
        self.password_regex = re.compile(
            r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'
        )

    def __call__(self, request):

        if request.method == "POST" and request.path in ["/signup/", "/login/"]:
            try:
                data = json.loads(request.body)
            except Exception:
                return JsonResponse({"error": "Invalid JSON"}, status=400)

            # common validation
            if request.path == "/signup/":
                username = data.get("username", "").strip()
                email = data.get("email", "").strip()
                password = data.get("password", "").strip()

                if not username or not email or not password:
                    return JsonResponse({"error": "All fields are required"}, status=400)

                if not self.username_regex.fullmatch(username):
                    return JsonResponse({"error": "Invalid username"}, status=400)

                if not self.email_regex.fullmatch(email):
                    return JsonResponse({"error": "Invalid email format"}, status=400)

                if not self.password_regex.fullmatch(password):
                    return JsonResponse({"error": "Weak password"}, status=400)

            if request.path == "/login/":
                if not data.get("username") or not data.get("password"):
                    return JsonResponse(
                        {"error": "Username and password required"}, status=400
                    )

        return self.get_response(request)
