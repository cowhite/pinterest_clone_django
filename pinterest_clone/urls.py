from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic import TemplateView

from dajaxice.core import dajaxice_autodiscover, dajaxice_config
dajaxice_autodiscover()

from core.views import ProfileView, HomeView


urlpatterns = patterns("",

    #url(r"^$", TemplateView.as_view(template_name="homepage.html"), name="home"),
    url(r"^$", HomeView.as_view(), name="home"),
    url(r"^admin/", include(admin.site.urls)),
    url(dajaxice_config.dajaxice_url, include('dajaxice.urls')),
    
    url(r"^account/", include("account.urls")),
    url(r"^(?P<username>[a-zA-Z0-9_]+)/$", ProfileView.as_view(),
        name="user-profile"),

    url(r'^avatar/', include('avatar.urls')),
    url(r"^", include("core.urls")),
    
)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()
