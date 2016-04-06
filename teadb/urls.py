from django.conf.urls import url
from django.contrib import admin

from tea.views import IndexView, TeaDetailView, CreateReviewView, AddTeaView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',IndexView.as_view(), name='index'),
    url(r'^tea/(?P<pk>[0-9]+)/$', TeaDetailView.as_view(), name='tea_detail'),
    url(r'^tea/(?P<pk>[0-9]+)/reviews/create/$', CreateReviewView.as_view(), name='create_review'),
    url(r'^tea/add/$', AddTeaView.as_view(), name='add_tea'),
]
