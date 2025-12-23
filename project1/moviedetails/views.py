from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from moviedetails.models import MovieBooking
# Create your views here.

@csrf_exempt
def BookMyshow(request):
    try:
        if request.method == "POST":
            data = json.loads(request.body)
            moviedetails = MovieBooking.objects.create(
                moviename = data.get("movie_name"),
                showtime = data.get("show_time"),
                screenname = data.get("screen_name")
            )
            return JsonResponse({"status":"success","message":"book succesfully","transcation_id":moviedetails.transcationid},status = 201)
        else:
            return JsonResponse({"error":"only post method is allowed"},status = 405)
    except Exception as e:
        return JsonResponse({"status":"error","message":str(e)},status = 400)
            

def get_all_movies(request):
    movies = MovieBooking.objects.all()
    total = MovieBooking.objects.count()

    data = []
    for movie in movies :
        data.append(
            {
                "moviename":movie.moviename,
                "showtime":movie.showtime,
                "screenname":movie.screenname,
                "transcationid":str(movie.transcationid),
                "dateandtime":movie.dateandtime
            }
        )
    return JsonResponse({"status":"success","data":data,"total-records":total,"filter-screen3":MovieBooking.objects.filter(screenname="screen-3").count()},safe=False)

