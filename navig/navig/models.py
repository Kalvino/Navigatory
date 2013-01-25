from itertools import product
from django.contrib.auth.models import User
from django.db import models

from django.utils.translation import ugettext as _
from transmeta import TransMeta
from stdimage.fields import StdImageField


class ActiveManager(models.Manager):
    """
    Manager class that returns active records
    """
    def get_query_set(self):
        return super(ActiveManager, self).get_query_set().filter(is_active=True)


class CommonMixin(models.Model):
    """
    Abstract base class for common information
    """
    is_active       = models.BooleanField(default=True)
    last_active     = models.DateField(auto_now=True)
    date            = models.DateField(auto_now_add=True)

    objects     = models.Manager()
    active      = ActiveManager()

    class Meta:
        abstract = True


class ImageMixin(models.Model):
    width = models.IntegerField(blank=True, null=True, editable=False)
    height = models.IntegerField(blank=True, null=True, editable=False)

    def save(self, *args, **kwargs):
        try:
            this = ImageMixin.objects.get(id=self.id)
            if this.image != self.image:
                this.image.delete(save=False)
        except: pass # when new photo then we do nothing, normal case
        super(ImageMixin, self).save(args, kwargs)

    def delete(self, using=None):
        super(ImageMixin, self).delete(using)
        self.image.delete(save=False)

    class Meta:
        abstract = True


class StaticPage(models.Model):
    __metaclass__ = TransMeta

    name = models.CharField(max_length=255, verbose_name=_("Name"))
    content = models.TextField(verbose_name=_("Name"))

    def __unicode__(self):
        return self.name

    class Meta:
        translate = ('content',)


class Site(CommonMixin, ImageMixin):
    __metaclass__ = TransMeta

    name = models.CharField(max_length=255, verbose_name=_("Name"))
    description = models.TextField(verbose_name=_("Description"))
    has_airport = models.BooleanField(default=False)
    rating = models.IntegerField()
    order = models.IntegerField()
    do_not_miss = models.TextField(verbose_name=_("Do not miss"))
    recommended_stay = models.TextField(verbose_name=_("Recommended stay"))
    address = models.CharField(max_length=255, verbose_name=_("Address"))
    state = models.CharField(max_length=100, verbose_name=_("State"))
    price = models.TextField(verbose_name=_("Price"))
    good_to_know = models.TextField(verbose_name=_("Good to know"))
    link = models.URLField(blank=True, null=True)
    region = models.ManyToManyField('Region', blank=True, null=True)
    interests = models.ManyToManyField('Interest', blank=True, null=True)
    map = StdImageField(
        upload_to='uploaded_images/%Y/%m/%d',
        max_length=255,
        height_field='height',
        width_field='width',
        size=(453, 294, True),
        thumbnail_size=(195, 150, True),
        blank=True,
        null=True
    )
    location_lat = models.DecimalField(
        u'Location (latitude)', max_digits=10, decimal_places=7, default=0,
        help_text=u"You can use http://www.getlatlon.com to get a location's coordinates"
    )
    location_lon = models.DecimalField(
        u'Location (longitude)', max_digits=10, decimal_places=7, default=0,
        help_text=u"You can use http://www.getlatlon.com to get a location's coordinates"
    )


    def get_next(self):
        next = Site.objects.filter(id__gt=self.id)
        if next:
          return next[0]
        return False


    def get_prev(self):
        prev = Site.objects.filter(id__lt=self.id)
        if prev:
          return prev[0]
        return False


    def __unicode__(self):
        return self.name


    @models.permalink
    def get_url(self):
        return ('sitedetails', (), { 'pk': self.id })


    class Meta:
        translate = (
            'description',
            'do_not_miss',
            'recommended_stay',
            'address',
            'state',
            'price',
            'good_to_know',
        )


class SiteImage(CommonMixin, ImageMixin):
    site = models.ForeignKey('Site')
    image = StdImageField(
        upload_to='uploaded_images/%Y/%m/%d',
        max_length=255,
        height_field='height',
        width_field='width',
        size=(246, 160, True),
        thumbnail_size=(200, 148, True),
        blank=True,
        null=True
    )

    def __unicode__(self):
        return u"%s image" % self.site.name


class SiteActivity(CommonMixin, ImageMixin):
    __metaclass__ = TransMeta


    site = models.ForeignKey('Site')
    name = models.CharField(max_length=255, verbose_name=_("Name"))
    description = models.TextField(verbose_name=_("Description"))
    price = models.CharField(max_length=100)
    image = StdImageField(
        upload_to='uploaded_images/%Y/%m/%d',
        max_length=255,
        height_field='height',
        width_field='width',
        size=(183, 112, True),
        blank=True,
        null=True
    )

    def __unicode__(self):
        return self.name

    class Meta:
        translate = ('name', 'description')


class SiteActivityImage(CommonMixin, ImageMixin):
    site_activity = models.ForeignKey('SiteActivity')
    image = StdImageField(
        upload_to='uploaded_images/%Y/%m/%d',
        max_length=255,
        height_field='height',
        width_field='width',
        size=(266, 175, True),
        blank=True,
        null=True
    )

    def __unicode__(self):
        return u"%s image" % self.site_activity.name


class SiteHotel(CommonMixin):
    __metaclass__ = TransMeta

    name = models.CharField(max_length=255, verbose_name=_("Name"))
    description = models.TextField(verbose_name=_("Description"))
    price = models.FloatField()

    def __unicode__(self):
        return self.name

    class Meta:
        translate = ('name', 'description')


#class SiteCar(CommonMixin):
#    __metaclass__ = TransMeta
#
#    name = models.CharField(max_length=255)
#    description = models.TextField()
#
#    class Meta:
#        translate = ('name', 'description')


class Itinerary(CommonMixin):
    __metaclass__ = TransMeta

    user = models.ForeignKey(User, blank=True, null=True)
    session_key = models.CharField(max_length=50, blank=True, null=True)
    name = models.CharField(max_length=255, verbose_name=_("Name"))
    description = models.TextField(verbose_name=_("Description"), blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    sites = models.ManyToManyField('Site', through='ItinerarySite')

    def __unicode__(self):
        return self.name

    class Meta:
        translate = ('name', 'description')


class ItinerarySite(CommonMixin):
    # @todo: find out if car field should be added
    itinerary = models.ForeignKey('Itinerary')
    site = models.ForeignKey('Site')
    nights = models.IntegerField()
    order = models.IntegerField()
    start_date = models.DateField(blank=True, null=True)
    # @todo: you can book multiple hotels
    # hotel = models.ForeignKey('SiteHotel', blank=True, null=True)
    activities = models.ManyToManyField('SiteActivity', through='ItineraryPlaceActivity')

    def __unicode__(self):
        return u"%s - %s" % (self.itinerary.name, self.site.name)

    class Meta:
        ordering = ['order']


class ItineraryPlaceActivity(CommonMixin):
    site = models.ForeignKey('ItinerarySite')
    activity = models.ForeignKey('SiteActivity')
    is_booked = models.BooleanField(default=False)

    def __unicode__(self):
        return u"%s - %s - %s" % (self.site.itinerary.name, self.site.site.name, self.activity.name)


class Region(CommonMixin):
    name = models.CharField(max_length='255')

    def __unicode__(self):
        return self.name


class Interest(CommonMixin):
    __metaclass__ = TransMeta

    name = models.CharField(max_length='255', verbose_name=_("Name"))

    def __unicode__(self):
        return self.name

    class Meta:
        translate = ('name',)


class SiteComment(CommonMixin):
    user = models.ForeignKey(User)
    site = models.ForeignKey(Site)
    comment = models.TextField(verbose_name=_("Leave a comment"))

    def __unicode__(self):
        return 'Comment by %s' % self.user.username


class ExampleItinerary(CommonMixin, ImageMixin):
    __metaclass__ = TransMeta

    name = models.CharField(max_length=255, verbose_name=_("Name"))
    description = models.TextField(verbose_name=_("Description"), blank=True, null=True)
    map = StdImageField(
        upload_to='uploaded_images/%Y/%m/%d',
        max_length=255,
        height_field='height',
        width_field='width',
        size=(472, 306, True),
        thumbnail_size=(273, 150, True),
        blank=True,
        null=True
    )

    def get_next(self):
        next = Itinerary.objects.filter(id__gt=self.id)
        if next:
          return next[0]
        return False

    def get_prev(self):
        prev = Itinerary.objects.filter(id__lt=self.id)
        if prev:
          return prev[0]
        return False

    class Meta:
        translate = ('name', 'description')


class ExampleItineraryImage(CommonMixin, ImageMixin):
    example_itinerary = models.ForeignKey('ExampleItinerary')
    image = StdImageField(
        upload_to='uploaded_images/%Y/%m/%d',
        max_length=255,
        height_field='height',
        width_field='width',
        size=(246, 160, True),
        blank=True,
        null=True
    )

    def __unicode__(self):
        return u"%s image" % self.example_itinerary.name


class ExampleItinerarySite(CommonMixin):
    example_itinerary = models.ForeignKey('ExampleItinerary')
    day_number = models.IntegerField()
    from_site = models.ForeignKey('Site', related_name='+')
    to_site = models.ForeignKey('Site', related_name='+')


class ExampleItinerarySiteDetail(models.Model):
    example_itinerary_site = models.ForeignKey('ExampleItinerarySite')
    description = models.CharField(max_length=255)


class ExampleItinerarySiteActivity(models.Model):
    example_itinerary_site = models.ForeignKey('ExampleItinerarySite')
    activity = models.ForeignKey('SiteActivity')


class Session(models.Model):
    key = models.CharField(max_length=50)


class Segment(models.Model):
    distance = models.FloatField(verbose_name=_("Driving Hours"))
    segment = models.IntegerField()
    sites = models.ManyToManyField('Site')

    def __unicode__(self):
        return u"Segment %s" % self.segment


class Route(models.Model):
    route = models.IntegerField()
    segments = models.ManyToManyField('Segment')

    def __unicode__(self):
        return u"Route %s" % self.route


class RecommendedItinerary(ImageMixin):
    __metaclass__ = TransMeta

    name = models.CharField(max_length=100, verbose_name=_("Name"))
    description = models.TextField(verbose_name=_("Description"), blank=True, null=True)
    routes = models.ManyToManyField('Route')
    map = StdImageField(
        upload_to='uploaded_images/%Y/%m/%d',
        max_length=255,
        height_field='height',
        width_field='width',
        size=(472, 306, True),
        thumbnail_size=(273, 150, True),
        blank=True,
        null=True
    )

    def __unicode__(self):
        return u"%s" % self.name

    def save(self, *args, **kwargs):
        super(RecommendedItinerary, self).save(*args, **kwargs)
        # Remove previously generated data
        RecommendedItineraryCombinations.objects.filter(recommended_itinerary__pk=self.pk).delete()
        # Generate new data
        route_segment_sets = []
        for route in self.routes.all():
            route_segment_sets.append(route.segments.all())

        segment_products = list(product(*route_segment_sets))
        for segment_product in segment_products:
            sites = []
            distance = 0
            for segment in segment_product:
                if segment.distance: distance += segment.distance
                sites.extend(segment.sites.all())

            itinerary_combinations = RecommendedItineraryCombinations.objects.create(
                recommended_itinerary=self,
                distance=distance,
                nights=len(sites),
                starting_point=sites[0],
                ending_point=sites[-1],
            )
            itinerary_combinations.sites.add(*sites)

    class Meta:
        translate = ('name', 'description')

class RecommendedItineraryCombinations(models.Model):
    recommended_itinerary = models.ForeignKey('RecommendedItinerary')
    sites = models.ManyToManyField('Site')
    distance = models.IntegerField()
    nights = models.IntegerField()
    starting_point = models.ForeignKey('Site', related_name='+')
    ending_point = models.ForeignKey('Site', related_name='+')

    def __unicode__(self):
        return u"%s combinations" % self.recommended_itinerary.name


class Distance(models.Model):
    point_a = models.ForeignKey('Site', related_name='+')
    point_b = models.ForeignKey('Site', related_name='+')
    distance = models.FloatField()
    hours = models.FloatField()