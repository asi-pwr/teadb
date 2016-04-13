from django.forms import ModelForm
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views.generic import ListView, DetailView, FormView
from tea.models import Tea, Review, TeaType


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


class TeaAddForm(ModelForm):
    class Meta:
        model = Tea
        fields = ['name', 'type', 'description', 'region']


class AddTeaView(FormView):
    form_class = TeaAddForm
    template_name = 'tea/add_tea.html'
    success_url = '/'

    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect(reverse('index'))


class TeaTypeAddForm(ModelForm):
    class Meta:
        model = TeaType
        fields = ['tea_type']


class AddTeaTypeView(FormView):
    form_class = TeaTypeAddForm
    template_name = 'tea/add_tea_type.html'
    success_url = '/'

    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect(reverse('index'))
