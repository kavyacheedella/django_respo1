from django.shortcuts import render
from django.http import JsonResponse
from .decorators import hall_ticket_required, exam_fee_required
from .models import StudentProfile

# Create your views here.

@hall_ticket_required
@exam_fee_required
def attend_exam(request):
    profile = StudentProfile.objects.get(user=request.user)

    if profile.attendance_percentage < 75:
        return JsonResponse(
            {"error": "Attendance below 75%"},
            status=403
        )

    return JsonResponse(
        {"message": "Student allowed to attend exam"},
        status=200
    )
