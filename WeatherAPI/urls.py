from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from django.views.generic.base import RedirectView

from RestAPI.views import *

urlpatterns = [
	url(r'^weather/$', WeatherView.as_view()),
    url(r'^erase/$', EraseView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
