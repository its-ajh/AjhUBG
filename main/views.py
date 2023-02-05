from django.shortcuts import render
from django.views import View
import json
  
# Create your views here.
class Index(View):
  def get(self, request, *args, **kwargs):
    # Opening JSON file
    f = open('games.json')
    data = json.load(f)
    context = {
      "data": data,
    }
    return render(request, "main/index.html", context);

class Detail(View):
   def get(self, request, pk, *args, **kwargs):
    # Opening JSON file
    f = open('games.json')
    data = json.load(f)[pk]
    context = {
      "data": data
    }
    return render(request, "main/detail.html", context);
