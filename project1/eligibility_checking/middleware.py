from django.http import JsonResponse

class LoginCheckMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Allow admin and static files
        if request.path.startswith('/admin/'):
            return self.get_response(request)
        
        if request.path == '/signup/':
            return self.get_response(request)

        # DEBUG (temporary) – add this print
        print("USER:", request.user, "AUTH:", request.user.is_authenticated)

        if not request.user.is_authenticated:
            return JsonResponse(
                {"error": "Login required to attend exam"},
                status=401
            )

        return self.get_response(request)

