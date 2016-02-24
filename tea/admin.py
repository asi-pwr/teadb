from django.contrib import admin

from tea.models import TeaType, Tea, Review

admin.site.register(TeaType)
admin.site.register(Tea)
admin.site.register(Review)