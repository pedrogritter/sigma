import json
from django.shortcuts import render

# Create your views here.
def landing(request):
    options = [("Home","http://sigma-alfa.herokuapp.com"), ("Aluno",""), ("Professor",""), ("About","")]

    items = []

    for option in options:
        items.append({
            "name" : option[0],
            "url" : option[1],
        })

    context = {}
    context["items_json"] = json.dumps(items)

    return render(request,'pages/landing.html',context)
