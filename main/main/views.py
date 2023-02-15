from django.shortcuts import render
from django.views import View
import json
import markdown2
from django.db.models import Q
from jsoncommands.blacklistmail import *
from .models import *
from .forms import *
# Create your views here.
class Index(View):
  def get(self, request, *args, **kwargs):
    # Opening JSON file
    f = open('games.json')
    data = json.load(f)
    if request.user.is_authenticated:
      if not JsonMailFilterDeny("blacklist.json", request.user.email):
        return render(request, "main/denied.html");
    context = {
      "data": data,
    }
    return render(request, "main/index.html", context);

class Detail(View):
   def get(self, request, pk, *args, **kwargs):
    # Opening JSON file
    f = open('games.json');
    comment = Comments.objects.filter(at_game=pk).order_by("-date_created")
    data = json.load(f)[pk]
    form = Comment()
    context = {
      "form": form,
      "comment": comment,
      "data": data,
    }
    return render(request, "main/detail.html", context);
   def post(self, request, pk, *args, **kwargs):
       # Opening JSON file
      f = open('games.json');
      comment = Comments.objects.filter(at_game=pk).order_by("-date_created")
      data = json.load(f)[pk]
      form = Comment(request.POST)
      if form.is_valid():
            new_post = form.save(commit=False)
            new_post.at_game = pk
            new_post.user = request.user
            new_post.save()
      context = {
        "form": form,
        "comment": comment,
        "data": data
      }
      return render(request, "main/detail.html", context);

class Links(View):
  def get(self, request, *args, **kwargs):
    return render(request, "main/links.html");

class Changelog(View):
  def get(self, request, *args, **kwargs):
    # Opening JSON file
    with open('changelog.md', 'r') as f:
      tempMd= f.read()
    log = markdown2.markdown(str(tempMd));
    context = {
      "log": log
    }
    return render(request, "main/changelog.html", context);

def chain(*iterables):
    # chain('ABC', 'DEF') --> A B C D E F
    for it in iterables:
        for element in it:
            yield element
class Search(View):
    def get(self, request, *args, **kwargs):
        query = self.request.GET.get("q")
        f = open('games.json');
        data = json.load(f)
        context = {
          "data": data,
          "query": query
        }
        return render(request, 'main/search.html', context)
