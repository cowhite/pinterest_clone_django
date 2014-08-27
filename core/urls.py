from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.views.generic import TemplateView

from django.contrib import admin

from .views import BoardFormView


urlpatterns = patterns("core.views",
    url(r"^board/new/$", BoardFormView.as_view(), name="new-board"),
)
