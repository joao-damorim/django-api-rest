from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CreateView
from .views import DetailsView
from .views import CreateViewTeste
from .views import DetailsViewTeste

urlpatterns = {
    url(r'^bucketlists/$', CreateView.as_view(), name="create"),
    url(r'^bucketlists/(?P<pk>[0-9]+)/$',
        DetailsView.as_view(), name="details"),
    url(r'^teste/$', CreateViewTeste.as_view(), name="create"),
    url(r'^teste/(?P<pk>[0-9]+)/$',
        DetailsViewTeste.as_view(), name="details"),
}

urlpatterns = format_suffix_patterns(urlpatterns)