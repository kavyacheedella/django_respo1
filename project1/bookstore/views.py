from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
import json
import re
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

@csrf_exempt
def update_book_details(request):
    try:
        if (request.method=="PUT"):
            data = json.loads(request.body)
            ref_author = data.get("Author")
            new_price = data.get("new_price")
            update = Bookstore.objects.filter(Author=ref_author).update(Price = new_price)
            if update==0:
                msg = "no records found"
            else:
                msg = "record updated successfully"    
            return JsonResponse({"status":"success","msg":msg},status=200)
        return JsonResponse({"status":"failure","msg":"only put method is allowed"},status = 400)
    except Exception as e:
        return JsonResponse({"status":"error","message":str(e)},status=500)

@csrf_exempt
def del_book_details(request,ref_author):
    try:
        if (request.method == "DELETE"):
            delete = Bookstore.objects.filter(Author=ref_author).delete()
            if delete[0] == 0:
                msg = "no records found"
            else:
                msg = "record deleted successfully"
            return JsonResponse({"status":"success","msg":msg},status=200)
        return JsonResponse({"status":"failure","msg":"only delete method is allowed"},status=400)
    except Exception as e:
        return JsonResponse({"status":"error","message":str(e)},status=500)



# | Symbol  | Meaning          |    |
# | ------- | ---------------- | -- |
# | `^`     | Start of string  |    |
# | `$`     | End of string    |    |
# | `.`     | Any character    |    |
# | `*`     | 0 or more        |    |
# | `+`     | 1 or more        |    |
# | `?`     | 0 or 1           |    |
# | `{n}`   | Exactly n times  |    |
# | `{n,}`  | At least n times |    |
# | `{n,m}` | Between n and m  |    |
# | `[]`    | Character set    |    |
# | `()`    | Grouping         |    |
# | `       | `                | OR |
# | `\d`    | Digit            |    |
# | `\w`    | Word character   |    |
# | `\s`    | Space            |    |


# | Function         | Purpose            |
# | ---------------- | ------------------ |
# | `re.match()`     | Match from start   |
# | `re.fullmatch()` | Match whole string |
# | `re.search()`    | Search anywhere    |
# | `re.findall()`   | Get all matches    |
# | `re.finditer()`  | Iterate matches    |
# | `re.sub()`       | Replace text       |
# | `re.split()`     | Split text         |


# | Task           | Best Function    |
# | -------------- | ---------------- |
# | Validate input | `re.fullmatch()` |
# | Search text    | `re.search()`    |
# | Extract data   | `re.findall()`   |
# | Replace text   | `re.sub()`       |
# | Split text     | `re.split()`     |



@csrf_exempt
def update_book_by_author_regex(request):

    # Allow only PUT method
    if request.method != "PUT":
        return JsonResponse(
            {"status": "failure", "message": "Only PUT method is allowed"},
            status=405
        )

    try:
        data = json.loads(request.body.decode("utf-8"))

        author = data.get("Author")
        new_price = data.get("new_price")

        # Validate required fields
        if not author or new_price is None:
            return JsonResponse(
                {"status": "failure", "message": "Author and new_price are required"},
                status=400
            )

        # Regex validation for author name
        author_pattern = r'(?i)^[A-Za-z\. ]+$'
        if not re.match(author_pattern, author):
            return JsonResponse(
                {"status": "failure", "message": "Invalid author name format"},
                status=400
            )

        # Update using regex (exact match but validated)
        updated_count = Bookstore.objects.filter(
            Author__regex=rf'^{re.escape(author)}$'
        ).update(Price=new_price)

        if updated_count == 0:
            return JsonResponse(
                {"status": "failure", "message": "No records found"},
                status=404
            )

        return JsonResponse(
            {
                "status": "success",
                "message": "Book price updated successfully",
                "updated_records": updated_count
            },
            status=200
        )

    except Exception as e:
        return JsonResponse(
            {"status": "error", "message": str(e)},
            status=500
        )
    

@csrf_exempt
def delete_book_by_author_regex(request):

    # Allow only DELETE method
    if request.method != "DELETE":
        return JsonResponse(
            {"status": "failure", "message": "Only DELETE method is allowed"},
            status=405
        )

    try:
        data = json.loads(request.body.decode("utf-8"))
        author = data.get("Author")

        # Check author present
        if not author:
            return JsonResponse(
                {"status": "failure", "message": "Author is required"},
                status=400
            )

        # Regex validation for author name
        author_pattern = r'^[A-Za-z]+(?:[\. ]+[A-Za-z]+)*$'

        if not re.match(author_pattern, author ,re.IGNORECASE):
            return JsonResponse(
                {"status": "failure", "message": "Invalid author name format"},
                status=400
            )

        # Safe regex delete (exact author match)
        deleted_count = Bookstore.objects.filter(
            Author__regex=rf'^{re.escape(author)}$'
        ).delete()

        if deleted_count == 0:
            return JsonResponse(
                {"status": "failure", "message": "No records found"},
                status=404
            )

        return JsonResponse(
            {
                "status": "success",
                "message": f"{deleted_count} record(s) deleted successfully"
            },
            status=200
        )

    except Exception as e:
        return JsonResponse(
            {"status": "error", "message": str(e)},
            status=500
        )