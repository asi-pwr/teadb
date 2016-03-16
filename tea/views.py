from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from tea.models import Tea, Review


class IndexView(ListView):
    template_name = "tea/index.html"
    model = Tea


class TeaDetailView(DetailView):
    template_name = "tea/tea_detail.html"
    model = Tea


class ReviewView(ListView):
    template_name = 'tea/tea_reviews.html'
    model = Review


class CreateReviewView(CreateView):
    template_name = 'tea/create_review.html'
    model = Review
    fields = ['content','author']
