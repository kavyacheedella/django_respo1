from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from bookstore.models import Bookstore
# Create your views here.

@csrf_exempt
def bookdetails(request):
    try:
        if(request.method=='POST'):
            data = json.loads(request.body)
            details = Bookstore.objects.create(
                Bookname = data.get("book_name"),
                Author = data.get("author_name"),
                Price = data.get("price"),
                Rating = data.get("rating"),
                Category = data.get("category")
            )
            return JsonResponse({"status":"success","data":data},status = 201)
        
        else:
            return JsonResponse({"error":"only POST method is allowed"},status = 400)
    except Exception as e:
        return JsonResponse({"status":"error","message":str(e)},status=405)
        

def get_details(request):
    books_details = Bookstore.objects.all()
    total = Bookstore.objects.count()

    data = []
    for book in books_details:
        data.append(
            {
                "bookname":book.Bookname,
                "authorname":book.Author,
                "price":book.Price,
                "category":book.Category,
                "rating":book.Rating
            }
        )
        return JsonResponse({"status":"success","data":data,"total-books":total})
