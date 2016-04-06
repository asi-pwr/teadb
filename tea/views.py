from django.forms import ModelForm
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views.generic import ListView, DetailView, FormView
from tea.models import Tea, Review


class IndexView(ListView):
    template_name = "tea/index.html"
    model = Tea


class TeaDetailView(DetailView):
    template_name = "tea/tea_detail.html"
    model = Tea


class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['content', 'author']


class CreateReviewView(FormView):
    form_class = ReviewForm
    template_name = 'tea/create_review.html'

    def form_valid(self, form):
        review = form.save(commit=False)
        review.reviewed_tea = Tea.objects.get(id=self.kwargs['pk'])
        review.save()
        return HttpResponseRedirect(reverse('tea_detail', args=(self.kwargs['pk'])))

    def get_context_data(self, **kwargs):
        context = super(CreateReviewView, self).get_context_data(**kwargs)
        context['tea'] = Tea.objects.get(id=self.kwargs['pk'])
        return context
