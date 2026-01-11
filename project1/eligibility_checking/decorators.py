from django.http import JsonResponse
from .models import StudentProfile

def hall_ticket_required(view_func):
    def wrapper(request, *args, **kwargs):
        try:
            profile = StudentProfile.objects.get(user=request.user)
        except StudentProfile.DoesNotExist:
            return JsonResponse(
                {"error": "Student profile not found"},
                status=404
            )

        if not profile.has_hall_ticket:
            return JsonResponse(
                {"error": "Hall ticket not issued"},
                status=403
            )

        return view_func(request, *args, **kwargs)
    return wrapper


def exam_fee_required(view_func):
    def wrapper(request, *args, **kwargs):
        try:
            profile = StudentProfile.objects.get(user=request.user)
        except StudentProfile.DoesNotExist:
            return JsonResponse(
                {"error": "Student profile not found"},
                status=404
            )

        if not profile.exam_fee_paid:
            return JsonResponse(
                {"error": "Exam fee not paid"},
                status=403
            )

        return view_func(request, *args, **kwargs)
    return wrapper
