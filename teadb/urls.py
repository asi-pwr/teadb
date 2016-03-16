from django.conf.urls import url
from django.contrib import admin

from tea.views import IndexView, ReviewView, TeaDetailView, CreateReviewView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',IndexView.as_view(), name='index'),
    url(r'^tea/(?P<pk>[0-9]+)/$', TeaDetailView.as_view(), name='tea_detail'),
    url(r'^tea/(?P<pk>[0-9]+)/reviews/$', ReviewView.as_view(), name='tea_reviews'),
]
