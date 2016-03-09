from django.conf.urls import url
from django.contrib import admin

from tea.views import IndexView, ReviewView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',IndexView.as_view()),
    url(r'^tea/reviews/(?P<id>[0-9]+)/$', ReviewView.as_view()),
]
