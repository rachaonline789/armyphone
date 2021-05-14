from django.shortcuts import render
from django.views.generic import ListView
from .models import tb_army_phone
import json

# Create your views here.

class InfoListView(ListView):
    model = tb_army_phone
    template_name = 'infos/main.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["qs_json"] = json.dumps(list(tb_army_phone.objects.values()))
        return context
    