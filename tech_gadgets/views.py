from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse, HttpResponseNotFound, Http404
import json
from django.utils.text import slugify
from django.urls import reverse

from django.views import View
from django.views.generic.base import RedirectView

from .dummy_data import gadgets, manufacturers

# Create your views here.

def startpage_view(request):
    return render(request, 'tech_gadgets/test.html', {'gadget_list': gadgets})

class RedirectToGadgetView(RedirectView):
    pattern_name = "gadget_slug_url"

    def get_redirect_url(self, *args, **kwargs):
        slug = slugify(gadgets[kwargs.get("gadget_id",0)]["name"])
        new_kwargs = {"gadget_slug": slug} 
        return super().get_redirect_url(*args, **new_kwargs)

def single_gadget_int_view(request,gadget_id):
    if len(gadgets) > gadget_id:
        new_slug = slugify(gadgets[gadget_id]["name"])
        new_url = reverse("gadget_slug_url", args=[new_slug])
        return redirect(new_url)
    return HttpResponseNotFound("not found")

""" return JsonResponse({"result": slugify(gadgets[1]['name'])}) """
""" return JsonResponse(gadgets[gadget_id]) """

class GadgetView(View):
    def get(self, request, gadget_slug):
        gadget_match = None

        for gadget in gadgets:
            if slugify(gadget["name"]) == gadget_slug:
                gadget_match = gadget
        if gadget_match:        
            return JsonResponse(gadget_match)
        raise Http404()
    
    def post(self, request):
        try:
            data = json.loads(request.body)
            print(f"recieved data: {data}")
            return JsonResponse({"response": "Das war was"})
        except:
            return JsonResponse({"response": "Das war wohl nichts"})


""" def single_gadget_view(request, gadget_slug=""):

    if request.method == "GET":
        gadget_match = None

        for gadget in gadgets:
            if slugify(gadget["name"]) == gadget_slug:
                gadget_match = gadget
        if gadget_match:        
            return JsonResponse(gadget_match)
        raise Http404()

    if request.method == "POST":
        try:
            data = json.loads(request.body)
            print(f"recieved data: {data}")
            return JsonResponse({"response": "Das war was"})
        except:
            return JsonResponse({"response": "Das war wohl nichts"}) """

""" HttpResponse(json.dumps(gadgets[0]), content_type = "application/json") Lange Form, wird durch JsonResponse gekürzt """


class RedirectToManufacturertView(RedirectView):
    pattern_name = "manufacturer_slug_url"

    def get_redirect_url(self, *args, **kwargs):
        slug = slugify(manufacturers[kwargs.get("manufacturer_id",0)]["name"])
        new_kwargs = {"manufacturer_slug": slug} 
        return super().get_redirect_url(*args, **new_kwargs)

class ManufacturerView(View):
    def get(self, request, manufacturer_slug):
        manufacturer_match = None

        for manufacturer in manufacturers:
            if slugify(manufacturer["name"]) == manufacturer_slug:
                manufacturer_match = manufacturer
        if manufacturer_match:        
            return JsonResponse(manufacturer_match)
        raise Http404()
    
    def post(self, request):
        try:
            data = json.loads(request.body)
            print(f"recieved data: {data}")
            return JsonResponse({"response": "Das war was"})
        except:
            return JsonResponse({"response": "Das war wohl nichts"})
        

def single_manufacturer_int_view(request, manufacturer_id):
    if len(manufacturers) > manufacturer_id:
        new_slug = slugify(manufacturers[manufacturer_id]["name"])
        new_url = reverse("manufacturer_slug_url", args=[new_slug])
        return redirect(new_url)
    return HttpResponseNotFound("not found")