from django.conf.urls import url
from django.contrib import admin

from tea.views import IndexView, ReviewView, TeaDetailView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',IndexView.as_view()),
    url(r'^tea/(?P<pk>[0-9]+)/$', TeaDetailView.as_view()),
    url(r'^tea/reviews/(?P<pk>[0-9]+)/$', ReviewView.as_view()),
]
