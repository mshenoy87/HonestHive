from django.http import HttpResponse, Http404, JsonResponse
from django.shortcuts import render

from Waggles.models import Waggle

def home_page(request, *args, **kwargs):
   return HttpResponse("<h1>HelloWorld</h>")
    # return render(request, template_name="pages/homePage.html", context= {}, status=200)

# Create your views here.
def show_waggle(request, waggle_id, *args, **kwargs):
   # page we will be seeing goes here
    data = {
       "id": waggle_id,
    }
    status = 200
    try:
       waggleObject = Waggle.objects.get(id=waggle_id)
       data["content"] = waggleObject.waggleText
    except:
      data["message"] = "Not Found"
      status = 404
    #   raise Http404
    # renders the data from DB
    return JsonResponse(data, status=status)
    # return HttpResponse(f"<h1> {waggle_id} - {waggleObject.waggleText}</h>")