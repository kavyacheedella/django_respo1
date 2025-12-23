from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from orderdetails.models import OrderDetails

@csrf_exempt
def OrderPlacing(request):

    if request.method != "POST":
        return JsonResponse(
            {"error": "Only POST method is allowed"},
            status=405
        )

    try:
        data = json.loads(request.body.decode("utf-8"))

        details = OrderDetails.objects.create(
            username = data.get("user_name"),
            useremail = data.get("user_email"),   
            orderid = data.get("order_id"),
            amount = data.get("amount"),
            paymentmode = data.get("mode_of_payment"),
            status = "PLACED"                     
        )

        return JsonResponse(
            {
                "status": "success",
                "message": "order details saved",
                "transaction_id": str(details.transcationid)
            },
            status=201
        )

    except Exception as e:
        return JsonResponse(
            {"status": "error", "message": str(e)},
            status=400
        )
