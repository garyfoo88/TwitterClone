from django.shortcuts import render
from django.http import HttpResponse, Http404, JsonResponse
from .models import Tweet
# Create your views here.
def home_view(request, *args, **kwargs):
    return render(request, "pages/home.html", context={}, status=200)

def tweet_detail_view(request, id, *args, **kwargs):
    data = {
        "id": id
    }
    status = 200
    try:
        obj = Tweet.objects.get(id=id)
        data['content'] = obj.content
    except:
        data['message'] = "Not Found"
        status = 404

    

    return JsonResponse(data, status=status)