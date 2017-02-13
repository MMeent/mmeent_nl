from django.shortcuts import render

# Create your views here.
from django.views import View


class IndexView(View):
    template_name = 'base.html'

