# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'ExampleItinerary.description'
        db.delete_column('oxero_exampleitinerary', 'description')

        # Adding field 'ExampleItinerary.description_en'
        db.add_column('oxero_exampleitinerary', 'description_en',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'ExampleItinerary.description_fr'
        db.add_column('oxero_exampleitinerary', 'description_fr',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'ExampleItinerary.description'
        db.add_column('oxero_exampleitinerary', 'description',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Deleting field 'ExampleItinerary.description_en'
        db.delete_column('oxero_exampleitinerary', 'description_en')

        # Deleting field 'ExampleItinerary.description_fr'
        db.delete_column('oxero_exampleitinerary', 'description_fr')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'oxero.exampleitinerary': {
            'Meta': {'object_name': 'ExampleItinerary'},
            'date': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'description_fr': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'height': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'last_active': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            'map': ('stdimage.fields.StdImageField', [], {'thumbnail_size': "{'width': 273, 'force': True, 'height': 150}", 'upload_to': "'uploaded_images/%Y/%m/%d'", 'max_length': '255', 'blank': 'True', 'null': 'True', 'size': "{'width': 472, 'force': True, 'height': 306}"}),
            'name_en': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'name_fr': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'width': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'oxero.exampleitineraryimage': {
            'Meta': {'object_name': 'ExampleItineraryImage'},
            'date': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'example_itinerary': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['oxero.ExampleItinerary']"}),
            'height': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('stdimage.fields.StdImageField', [], {'blank': 'True', 'max_length': '255', 'null': 'True', 'upload_to': "'uploaded_images/%Y/%m/%d'", 'size': "{'width': 246, 'force': True, 'height': 160}"}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'last_active': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            'width': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'oxero.exampleitinerarysite': {
            'Meta': {'object_name': 'ExampleItinerarySite'},
            'date': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'day_number': ('django.db.models.fields.IntegerField', [], {}),
            'example_itinerary': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['oxero.ExampleItinerary']"}),
            'from_site': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'to': "orm['oxero.Site']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'last_active': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            'to_site': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'to': "orm['oxero.Site']"})
        },
        'oxero.exampleitinerarysiteactivity': {
            'Meta': {'object_name': 'ExampleItinerarySiteActivity'},
            'activity': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['oxero.SiteActivity']"}),
            'example_itinerary_site': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['oxero.ExampleItinerarySite']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'oxero.exampleitinerarysitedetail': {
            'Meta': {'object_name': 'ExampleItinerarySiteDetail'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'example_itinerary_site': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['oxero.ExampleItinerarySite']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
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
            'description_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'description_fr': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'last_active': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name_en': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'name_fr': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'sites': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['oxero.Site']", 'through': "orm['oxero.ItinerarySite']", 'symmetrical': 'False'}),
            'start_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
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
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'itinerary': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['oxero.Itinerary']"}),
            'last_active': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            'nights': ('django.db.models.fields.IntegerField', [], {}),
            'order': ('django.db.models.fields.IntegerField', [], {}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['oxero.Site']"}),
            'start_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'})
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
            'description_en': ('django.db.models.fields.TextField', [], {}),
            'description_fr': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'do_not_miss_en': ('django.db.models.fields.TextField', [], {}),
            'do_not_miss_fr': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'good_to_know_en': ('django.db.models.fields.TextField', [], {}),
            'good_to_know_fr': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'height': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'interests': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['oxero.Interest']", 'null': 'True', 'blank': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'last_active': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'map': ('stdimage.fields.StdImageField', [], {'thumbnail_size': "{'width': 195, 'force': True, 'height': 150}", 'upload_to': "'uploaded_images/%Y/%m/%d'", 'max_length': '255', 'blank': 'True', 'null': 'True', 'size': "{'width': 453, 'force': True, 'height': 294}"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'price_en': ('django.db.models.fields.TextField', [], {}),
            'price_fr': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'rating': ('django.db.models.fields.IntegerField', [], {}),
            'recommended_stay_en': ('django.db.models.fields.TextField', [], {}),
            'recommended_stay_fr': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'region': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['oxero.Region']", 'null': 'True', 'blank': 'True'}),
            'state_en': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'state_fr': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'width': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'oxero.siteactivity': {
            'Meta': {'object_name': 'SiteActivity'},
            'date': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description_en': ('django.db.models.fields.TextField', [], {}),
            'description_fr': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'height': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('stdimage.fields.StdImageField', [], {'blank': 'True', 'max_length': '255', 'null': 'True', 'upload_to': "'uploaded_images/%Y/%m/%d'", 'size': "{'width': 183, 'force': True, 'height': 112}"}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'last_active': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name_en': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'name_fr': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'price': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['oxero.Site']"}),
            'width': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'oxero.siteactivityimage': {
            'Meta': {'object_name': 'SiteActivityImage'},
            'date': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'height': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('stdimage.fields.StdImageField', [], {'blank': 'True', 'max_length': '255', 'null': 'True', 'upload_to': "'uploaded_images/%Y/%m/%d'", 'size': "{'width': 266, 'force': True, 'height': 175}"}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'last_active': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            'site_activity': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['oxero.SiteActivity']"}),
            'width': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'oxero.sitecomment': {
            'Meta': {'object_name': 'SiteComment'},
            'comment': ('django.db.models.fields.TextField', [], {}),
            'date': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'last_active': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['oxero.Site']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
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
            'image': ('stdimage.fields.StdImageField', [], {'thumbnail_size': "{'width': 200, 'force': True, 'height': 148}", 'upload_to': "'uploaded_images/%Y/%m/%d'", 'max_length': '255', 'blank': 'True', 'null': 'True', 'size': "{'width': 246, 'force': True, 'height': 160}"}),
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