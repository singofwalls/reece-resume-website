from django.http import HttpResponse
from django.views.generic import TemplateView

class index(TemplateView):
    template_name = "index.html"