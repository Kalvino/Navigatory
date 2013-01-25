from django.conf.urls import patterns, include, url
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.db.models.aggregates import Count
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.contrib.auth.views import password_reset_confirm
from oxero.models import ExampleItinerary
from oxero.views import (
    StaticPageView, SiteView, SiteDetailVeiw, ItineraryDetailVeiw,
    SetLanguageView, SearchView, ExploreView
)
from accounts.views import (
    RegistrationView, RegistrationConfirmView, LoginView, ResetPasswordView,
    LogoutView
)
from oxero.views import personalize

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^set_language/', SetLanguageView.as_view(), name='set_language'),
    url(r'^comments/', include('django.contrib.comments.urls')),
)

urlpatterns += i18n_patterns('',
    url(r'^$', ListView.as_view(
            template_name="index.html",
            queryset=ExampleItinerary.objects.annotate(
                num_days=Count('exampleitinerarysite')
            ),
            context_object_name='example_itineraries'
        ),
        name="home"
    ),
    url(r'^aboutus$',
        StaticPageView.as_view(template_name="aboutus"), name="aboutus"
    ),
    url(r'^advertising$',
        StaticPageView.as_view(template_name="advertising"), name="advertising"
    ),
    url(r'^contactus$',
        StaticPageView.as_view(template_name="contactus"), name="contactus"
    ),
    url(r'^explore$', ExploreView.as_view(), name="explore"),
    url(r'^info$',
        StaticPageView.as_view(template_name="info"), name="info"
    ),
    url(r'^itinerarydetails/(?P<pk>\d+)$',
        ItineraryDetailVeiw.as_view(), name="itinerarydetails"
    ),
    url(r'^itineraryexamples$', ListView.as_view(
            template_name="itineraryexamples.html",
            queryset=ExampleItinerary.objects.annotate(
                num_days=Count('exampleitinerarysite')
            ),
            context_object_name='example_itineraries'
        ),
        name="itineraryexamples"
    ),
    url(r'^legal$',
        StaticPageView.as_view(template_name="legal"), name="legal"
    ),
    url(r'^printpreview/(?P<pk>\d+)$',
        personalize.PrintPreview.as_view(),
        name="printpreview"
    ),
    url(r'^sitedetails/(?P<pk>\d+)$',
        SiteDetailVeiw.as_view(), name='sitedetails'
    ),
    url(r'^sites$', SiteView.as_view(), name="sites"),
    url(r'^registration$', RegistrationView.as_view(), name="registration"),
    url(r'^confirm_registration/(?P<id>\w+)/(?P<confirmation_hash>\w+)$',
        RegistrationConfirmView.as_view(), name="confirmregistration"
    ),
    url(r'^login$', LoginView.as_view(), name="login"),
    url(r'^logout$', LogoutView.as_view(), name="logout"),
    url(r'^reset_password$',
        ResetPasswordView.as_view(), name="resetpassword"
    ),
    url(r'^password/reset/confirm/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$',
        password_reset_confirm, {
            'template_name': 'password_reset_confirm.html',
            'post_reset_redirect': '/'
        },
        name='passwordresetconfirm'
    ),
    # Personalize urls
    url(r'^personalize$', personalize.ItineraryView.as_view(), name='personalize'),
    url(r'^personalize/itinerary$', personalize.ItineraryView.as_view()),
    url(r'^personalize/itinerary/(?P<id>\d+)$', personalize.ItineraryView.as_view(), name='viewcustomitinerary'),
    url(r'^personalize/itinerary/recommendation$', personalize.RecommendationView.as_view()),
    url(r'^personalize/itinerary_place/(?P<itinerary_id>\d+)$', personalize.ItineraryPlaceView.as_view()),
    url(r'^personalize/itinerary_place/(?P<itinerary_id>\d+)/site/(?P<site_id>\d+)$', personalize.ItineraryPlaceView.as_view()),
    url(r'^personalize/itinerary_place_activity/(?P<id>\d+)$', personalize.ItineraryPlaceActivityView.as_view()),
    url(r'^personalize/itinerary_place_activity/(?P<itinerary_id>\d+)-(?P<site_id>\d+)-(?P<activity_id>\d+)$', personalize.ItineraryPlaceActivityView.as_view()),
    url(r'^personalize/itinerary_place_hoteal$', personalize.ItineraryPlaceHotelView.as_view()),
    url(r'^personalize/itinerary_place_hoteal/(?P<id>\d+)$', personalize.ItineraryPlaceHotelView.as_view()),
    # Search
    url(r'^search$',
        SearchView.as_view(), name="search"
    ),
)
