from django.conf.urls import url
from django.contrib import admin

from tea.views import IndexView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',IndexView.as_view()),
]
