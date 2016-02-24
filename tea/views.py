from django.shortcuts import render
from django.views import generic
from tea.models import Tea


class IndexView(generic.ListView):
    template_name = "tea/index.html"
    model = Tea