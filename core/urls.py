from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.views.generic import TemplateView

from django.contrib import admin

from .views import BoardFormView, BoardView


urlpatterns = patterns("core.views",
    url(r"^board/new/$", BoardFormView.as_view(), name="new-board"),
    url(r"^(?P<username>[a-zA-Z0-9_]+)/(?P<board_slug>[a-zA-Z0-9_]+)/$",
        BoardView.as_view(),
        name="user-board"),
)
