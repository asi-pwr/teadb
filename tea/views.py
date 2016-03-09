from django.shortcuts import render
from django.views import generic
from tea.models import Tea, Review


class IndexView(generic.ListView):
    template_name = "tea/index.html"
    model = Tea


class ReviewView(generic.ListView):
    template_name = 'tea/tea_reviews.html'
    model = Review