from django.conf import settings
from django.core.urlresolvers import reverse
from django.db.models import Q
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from django.template.base import Template
from django.template.context import Context
from django.utils.translation import check_for_language
from django.views.generic.base import View
from oxero.models import StaticPage, Site, Interest, Region, ExampleItinerary
from oxero.forms import CommentForm

class SetLanguageView(View):
    def post(self, request):
        lang_code = request.POST.get('language', 'en')
        next = request.META.get('HTTP_REFERER', None)
        if next:
            next = '/%s/%s' % (lang_code, '/'.join(next.split('/')[4:]))
        else:
            next = '/'
        response = HttpResponseRedirect(next)
        if lang_code and check_for_language(lang_code):
            if hasattr(request, 'session'):
                request.session['django_language'] = lang_code
            else:
                response.set_cookie(settings.LANGUAGE_COOKIE_NAME, lang_code)
        return response

class StaticPageView(View):
    template_name = None

    def get(self, request):
        try:
            static_page = StaticPage.objects.get(name=self.template_name)
        except StaticPage.DoesNotExist:
            raise Http404

        t = Template(static_page.content)
        c = Context({'STATIC_URL': settings.STATIC_URL})

        return render(request, 'static_page.html', {
            'content': t.render(c)
        })


class SiteView(View):
    def get(self, request):
        region_filter = request.GET.getlist('region')
        interest_filter = request.GET.getlist('interest')

        sites = Site.objects.all()
        if region_filter: sites = sites.filter(region__in=region_filter)
        elif interest_filter: sites = sites.filter(interests__in=interest_filter)

        interests = Interest.objects.all()
        regions = Region.objects.all()

        return render(request, 'sites.html', {
            'sites': sites,
            'interests': interests,
            'regions': regions,
            'selected_regions': region_filter,
            'selected_interests': interest_filter
        })

class SiteDetailVeiw(View):
    def post(self, request, pk):
        try:
            site = Site.objects.select_related('SiteActivity', 'SiteImage').get(pk=pk)
        except Site.DoesNotExist:
            raise Http404

        form = CommentForm(data=request.POST)
        if form.is_valid():
            form.save(site=site, user=request.user)
            return HttpResponseRedirect(reverse('sitedetails', args=[pk]))

        else:
            return render(request, 'sitedetails.html', {
                'site': site,
                'form': form
            })

    def get(self, request, pk):
        try:
            site = Site.objects.select_related('SiteActivity', 'SiteImage').get(pk=pk)
        except Site.DoesNotExist:
            raise Http404
        places_close_by = []
        lower_order_sites = list(Site.objects.filter(order__lt=site.order))
        higher_order_sites = list(Site.objects.filter(order__gt=site.order))
        print '\033[91m', higher_order_sites, lower_order_sites, '\033[m'
        if lower_order_sites:
            places_close_by.append(lower_order_sites[0])

        elif higher_order_sites:
            places_close_by.append(higher_order_sites[-1])

        if higher_order_sites:
            places_close_by.append(higher_order_sites[0])
            if len(higher_order_sites) >= 2:
                places_close_by.append(higher_order_sites[1])
            elif lower_order_sites:
                places_close_by.append(lower_order_sites[0])
        form = CommentForm
        return render(request, 'sitedetails.html', {
            'places_close_by': places_close_by,
            'site': site,
            'form': form
        })


class ItineraryDetailVeiw(View):
    def get(self, request, pk):
        try:
            itinerary = ExampleItinerary.objects.get(pk=pk)
        except Site.DoesNotExist:
            raise Http404
        return render(request, 'itinerarydetails.html', {
            'itinerary': itinerary
        })


class SearchView(View):

    def get(self, request, id=None):
        # Init
        searchResults = None
        # Getting the query for search
        searchQuery = request.GET.get('query') or None
        if searchQuery is not None and searchQuery != '':
            # Performing the search for sites that matches the query
            searchResults = Site.objects.filter(
                Q(name__icontains=searchQuery) |
                Q(region__name__icontains=searchQuery) |
                Q(interests__name_en__icontains=searchQuery) |
                Q(interests__name_fr__icontains=searchQuery)
            ).select_related().distinct()
        # Response
        return render(request, 'search.html', {
            'searchQuery': searchQuery,
            'searchResults': searchResults,
        })


class ExploreView(View):

    def get(self, request):
        # Response
        return render(request, 'explore.html', {
            'allSites': Site.objects.all().only(
                'name', 'location_lat', 'location_lon'
            ),
        })