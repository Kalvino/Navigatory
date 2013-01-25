# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ItineraryPlaceActivity'
        db.create_table('oxero_itineraryplaceactivity', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('is_active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('last_active', self.gf('django.db.models.fields.DateField')(auto_now=True, blank=True)),
            ('date', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
            ('site', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['oxero.ItinerarySite'])),
            ('activity', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['oxero.SiteActivity'])),
            ('is_booked', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('oxero', ['ItineraryPlaceActivity'])

        # Adding model 'ItinerarySite'
        db.create_table('oxero_itinerarysite', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('is_active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('last_active', self.gf('django.db.models.fields.DateField')(auto_now=True, blank=True)),
            ('date', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
            ('itinerary', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['oxero.Itinerary'])),
            ('site', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['oxero.Site'])),
            ('nights', self.gf('django.db.models.fields.IntegerField')()),
            ('order', self.gf('django.db.models.fields.IntegerField')()),
            ('start_date', self.gf('django.db.models.fields.DateField')()),
            ('hotel', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['oxero.SiteHotel'])),
        ))
        db.send_create_signal('oxero', ['ItinerarySite'])

        # Adding model 'Itinerary'
        db.create_table('oxero_itinerary', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('is_active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('last_active', self.gf('django.db.models.fields.DateField')(auto_now=True, blank=True)),
            ('date', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
            ('name_en', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('name_fr', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('description_en', self.gf('django.db.models.fields.TextField')()),
            ('description_fr', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('start_date', self.gf('django.db.models.fields.DateField')()),
            ('default_image', self.gf('django.db.models.fields.related.ForeignKey')(related_name='+', to=orm['oxero.ItineraryImage'])),
        ))
        db.send_create_signal('oxero', ['Itinerary'])

        # Adding model 'SiteActivity'
        db.create_table('oxero_siteactivity', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('is_active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('last_active', self.gf('django.db.models.fields.DateField')(auto_now=True, blank=True)),
            ('date', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=255)),
            ('width', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('height', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('name_en', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('name_fr', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('description_en', self.gf('django.db.models.fields.TextField')()),
            ('description_fr', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal('oxero', ['SiteActivity'])

        # Adding model 'SiteHotel'
        db.create_table('oxero_sitehotel', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('is_active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('last_active', self.gf('django.db.models.fields.DateField')(auto_now=True, blank=True)),
            ('date', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
            ('name_en', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('name_fr', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('description_en', self.gf('django.db.models.fields.TextField')()),
            ('description_fr', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('price', self.gf('django.db.models.fields.FloatField')()),
        ))
        db.send_create_signal('oxero', ['SiteHotel'])

        # Adding model 'SiteImage'
        db.create_table('oxero_siteimage', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('is_active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('last_active', self.gf('django.db.models.fields.DateField')(auto_now=True, blank=True)),
            ('date', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=255)),
            ('width', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('height', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('site', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['oxero.Site'])),
        ))
        db.send_create_signal('oxero', ['SiteImage'])

        # Adding model 'Interest'
        db.create_table('oxero_interest', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('is_active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('last_active', self.gf('django.db.models.fields.DateField')(auto_now=True, blank=True)),
            ('date', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
            ('name_en', self.gf('django.db.models.fields.CharField')(max_length='255')),
            ('name_fr', self.gf('django.db.models.fields.CharField')(max_length='255', null=True, blank=True)),
        ))
        db.send_create_signal('oxero', ['Interest'])

        # Adding model 'Site'
        db.create_table('oxero_site', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('is_active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('last_active', self.gf('django.db.models.fields.DateField')(auto_now=True, blank=True)),
            ('date', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('description_en', self.gf('django.db.models.fields.TextField')()),
            ('description_fr', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('default_image', self.gf('django.db.models.fields.related.ForeignKey')(related_name='+', to=orm['oxero.SiteImage'])),
            ('rating', self.gf('django.db.models.fields.FloatField')()),
            ('do_not_miss_en', self.gf('django.db.models.fields.TextField')()),
            ('do_not_miss_fr', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('recommended_stay_en', self.gf('django.db.models.fields.TextField')()),
            ('recommended_stay_fr', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('address_en', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('address_fr', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('state_en', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('state_fr', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('price_en', self.gf('django.db.models.fields.TextField')()),
            ('price_fr', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('good_to_know_en', self.gf('django.db.models.fields.TextField')()),
            ('good_to_know_fr', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('link', self.gf('django.db.models.fields.URLField')(max_length=200)),
        ))
        db.send_create_signal('oxero', ['Site'])

        # Adding M2M table for field interests on 'Site'
        db.create_table('oxero_site_interests', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('site', models.ForeignKey(orm['oxero.site'], null=False)),
            ('interest', models.ForeignKey(orm['oxero.interest'], null=False))
        ))
        db.create_unique('oxero_site_interests', ['site_id', 'interest_id'])

        # Adding model 'ItineraryImage'
        db.create_table('oxero_itineraryimage', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('is_active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('last_active', self.gf('django.db.models.fields.DateField')(auto_now=True, blank=True)),
            ('date', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=255)),
            ('width', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('height', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('itinerary', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['oxero.Itinerary'])),
        ))
        db.send_create_signal('oxero', ['ItineraryImage'])

        # Adding model 'Region'
        db.create_table('oxero_region', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('is_active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('last_active', self.gf('django.db.models.fields.DateField')(auto_now=True, blank=True)),
            ('date', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length='255')),
        ))
        db.send_create_signal('oxero', ['Region'])


    def backwards(self, orm):
        # Deleting model 'ItineraryPlaceActivity'
        db.delete_table('oxero_itineraryplaceactivity')

        # Deleting model 'ItinerarySite'
        db.delete_table('oxero_itinerarysite')

        # Deleting model 'Itinerary'
        db.delete_table('oxero_itinerary')

        # Deleting model 'SiteActivity'
        db.delete_table('oxero_siteactivity')

        # Deleting model 'SiteHotel'
        db.delete_table('oxero_sitehotel')

        # Deleting model 'SiteImage'
        db.delete_table('oxero_siteimage')

        # Deleting model 'Interest'
        db.delete_table('oxero_interest')

        # Deleting model 'Site'
        db.delete_table('oxero_site')

        # Removing M2M table for field interests on 'Site'
        db.delete_table('oxero_site_interests')

        # Deleting model 'ItineraryImage'
        db.delete_table('oxero_itineraryimage')

        # Deleting model 'Region'
        db.delete_table('oxero_region')


    models = {
        'oxero.interest': {
            'Meta': {'object_name': 'Interest'},
            'date': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'last_active': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name_en': ('django.db.models.fields.CharField', [], {'max_length': "'255'"}),
            'name_fr': ('django.db.models.fields.CharField', [], {'max_length': "'255'", 'null': 'True', 'blank': 'True'})
        },
        'oxero.itinerary': {
            'Meta': {'object_name': 'Itinerary'},
            'date': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'default_image': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'to': "orm['oxero.ItineraryImage']"}),
            'description_en': ('django.db.models.fields.TextField', [], {}),
            'description_fr': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'last_active': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name_en': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'name_fr': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'sites': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['oxero.Site']", 'through': "orm['oxero.ItinerarySite']", 'symmetrical': 'False'}),
            'start_date': ('django.db.models.fields.DateField', [], {})
        },
        'oxero.itineraryimage': {
            'Meta': {'object_name': 'ItineraryImage'},
            'date': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'height': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '255'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'itinerary': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['oxero.Itinerary']"}),
            'last_active': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            'width': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'oxero.itineraryplaceactivity': {
            'Meta': {'object_name': 'ItineraryPlaceActivity'},
            'activity': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['oxero.SiteActivity']"}),
            'date': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_booked': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_active': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['oxero.ItinerarySite']"})
        },
        'oxero.itinerarysite': {
            'Meta': {'object_name': 'ItinerarySite'},
            'activities': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['oxero.SiteActivity']", 'through': "orm['oxero.ItineraryPlaceActivity']", 'symmetrical': 'False'}),
            'date': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'hotel': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['oxero.SiteHotel']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'itinerary': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['oxero.Itinerary']"}),
            'last_active': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            'nights': ('django.db.models.fields.IntegerField', [], {}),
            'order': ('django.db.models.fields.IntegerField', [], {}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['oxero.Site']"}),
            'start_date': ('django.db.models.fields.DateField', [], {})
        },
        'oxero.region': {
            'Meta': {'object_name': 'Region'},
            'date': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'last_active': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': "'255'"})
        },
        'oxero.site': {
            'Meta': {'object_name': 'Site'},
            'address_en': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'address_fr': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'date': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'default_image': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'to': "orm['oxero.SiteImage']"}),
            'description_en': ('django.db.models.fields.TextField', [], {}),
            'description_fr': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'do_not_miss_en': ('django.db.models.fields.TextField', [], {}),
            'do_not_miss_fr': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'good_to_know_en': ('django.db.models.fields.TextField', [], {}),
            'good_to_know_fr': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'interests': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['oxero.Interest']", 'symmetrical': 'False'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'last_active': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'price_en': ('django.db.models.fields.TextField', [], {}),
            'price_fr': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'rating': ('django.db.models.fields.FloatField', [], {}),
            'recommended_stay_en': ('django.db.models.fields.TextField', [], {}),
            'recommended_stay_fr': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'state_en': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'state_fr': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        },
        'oxero.siteactivity': {
            'Meta': {'object_name': 'SiteActivity'},
            'date': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description_en': ('django.db.models.fields.TextField', [], {}),
            'description_fr': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'height': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '255'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'last_active': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name_en': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'name_fr': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'width': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'oxero.sitehotel': {
            'Meta': {'object_name': 'SiteHotel'},
            'date': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description_en': ('django.db.models.fields.TextField', [], {}),
            'description_fr': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'last_active': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name_en': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'name_fr': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'price': ('django.db.models.fields.FloatField', [], {})
        },
        'oxero.siteimage': {
            'Meta': {'object_name': 'SiteImage'},
            'date': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'height': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '255'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'last_active': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['oxero.Site']"}),
            'width': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'oxero.staticpage': {
            'Meta': {'object_name': 'StaticPage'},
            'content_en': ('django.db.models.fields.TextField', [], {}),
            'content_fr': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['oxero']