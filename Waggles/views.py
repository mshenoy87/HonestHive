from django.http import HttpResponse, Http404, JsonResponse
from django.shortcuts import render, redirect
from random import randint

from Waggles.models import Waggle
from Waggles.forms import WaggleForm

# Create your views here.
def home_page(request, *args, **kwargs):
    # What you should see when you come to the home page
    return render(request, template_name="pages/home_page.html", context= {}, status=200)

def waggle_create_view(request, *args, **kwargs):
   # Initializing a form for context for data being sent (if no data, pass None)
   form = WaggleForm(request.POST or None)
   next_url = request.POST.get("next") or None
   if form.is_valid():
      obj = form.save(commit=False)
      obj.save()
      if next_url != None:
         return redirect(next_url)
      form = WaggleForm()
   return render(request, 'components/forms.html', context = {"form": form})

# shows a waggle as a dumped json dictionary depending on the id
def show_waggle(request, waggle_id, *args, **kwargs):
   # Page we will be seeing goes here
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
    
    # Render a single waggle from the data from DB
    return JsonResponse(data, status=status)

def waggles_list_view(request, *args, **kwargs):
   query_set = Waggle.objects.all()
   # Save everything in database into a list of dictionaries
   waggle_list = [{"id": query.id, "waggleText": query.waggleText, "likes": randint(0, 10)} for query in query_set]
   data = {
      "response": waggle_list
   }
   return JsonResponse(data)