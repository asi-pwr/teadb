from django.template import Library

from tea.models import Tea
from tea.views import ReviewForm

register = Library()


@register.inclusion_tag('show_tea_reviews.html')
def show_tea_reviews(tea):
    reviews = tea.review_set.all()
    return {'reviews': reviews}


@register.inclusion_tag('show_create_review_form.html')
def show_create_review_form(tea_id):
    form = ReviewForm()
    return {'form': form, 'tea_id': tea_id}


@register.inclusion_tag('show_tea_detai.html')
def show_tea_detail(tea_id):
    tea = Tea.objects.get(id=tea_id)
    return {'tea': tea}
