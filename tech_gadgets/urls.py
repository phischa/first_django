from django.urls import path
from .views import startpage_view, single_gadget_int_view, \
GadgetView, RedirectToGadgetView, ManufacturerView, single_manufacturer_int_view, \
RedirectToManufacturertView

    
urlpatterns = [
    path('start/', startpage_view),
    path('', RedirectToGadgetView.as_view()),

    path('gadget/', GadgetView.as_view()),
    path('<int:gadget_id>', RedirectToGadgetView.as_view()),
    path('gadget/<int:gadget_id>', single_gadget_int_view),
    path('gadget/<slug:gadget_slug>', GadgetView.as_view(), name="gadget_slug_url"),

    path('manufacturer/', RedirectToManufacturertView.as_view()),
    path('manufacturer/<int:manufacturer_id>', single_manufacturer_int_view),
    path('manufacturer/<slug:manufacturer_slug>', ManufacturerView.as_view(), name="manufacturer_slug_url"),
]