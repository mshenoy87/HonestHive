from django.http import HttpResponse, Http404, JsonResponse
from django.shortcuts import render
from random import randint

from Waggles.models import Waggle


# Create your views here.
def home_page(request, *args, **kwargs):
    return render(request, template_name="pages/home_page.html", context= {}, status=200)

# shows a waggle as a dumped json dictionary depending on the id
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
    
    # renders the data from DB
    return JsonResponse(data, status=status)

def waggles_list_view(request, *args, **kwargs):
   query_set = Waggle.objects.all()
   waggle_list = [{"id": query.id, "waggleText": query.waggleText, "likes": randint(0, 10)} for query in query_set]
   data = {
      "response": waggle_list
   }
   return JsonResponse(data)