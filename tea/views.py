from django.forms import ModelForm
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, FormView
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


class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['content','author']


class CreateReviewView(FormView):
    form_class = ReviewForm
    template_name = 'tea/create_review.html'
    success_url = 'tea/tea_reviews.html'

    # def get_initial(self):
    #     initial = super(CreateReviewView, self).get_initial()
    #     initial['reviewed_tea']= self.kwargs['pk']
    #     return initial

    def form_valid(self, form):
        form.fields['reviewed_tea']=self.kwargs['pk']
        form.save()

