from django.urls import path, re_path
from . import views, api_views

app_name = "core"
urlpatterns = [
    ## API URLs Start ##
    re_path(
        r"^api/link/$",
        api_views.LinkCreateAPIView.as_view(),
        name="api_link_create",
    ),
    re_path(
        r"^api/link/(?P<code>[0-9a-z]+)/$",
        api_views.LinkRetrieveAPIView.as_view(),
        name="api_link_retrieve",
    ),
    re_path(
        r"^api/edit/(?P<token>[0-9a-f-]+)/$",
        api_views.LinkRetrieveEditAPIView.as_view(),
        name="api_link_edit",
    ),
    re_path(
        r"^api/stats/$",
        api_views.StatsView.as_view(),
        name="stats"
    ),

    # Normal URLs start
    re_path(
        r"(?P<code>[0-9a-z]+)/?$",
        views.RedirectCodeView.as_view(),
        name="redirect",
    ),
    re_path(
        r"",
        views.HomeView.as_view(),
        name="home",
    )
]
