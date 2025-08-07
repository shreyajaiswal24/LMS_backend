from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import GoogleMeetLink, Semester, NewsAndEvents


class NewsAndEventsAdmin(TranslationAdmin):
    pass


admin.site.register(Semester)
admin.site.register(GoogleMeetLink)
admin.site.register(NewsAndEvents, NewsAndEventsAdmin)
