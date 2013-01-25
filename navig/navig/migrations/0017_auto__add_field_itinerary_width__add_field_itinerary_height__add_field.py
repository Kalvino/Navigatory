# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Itinerary.width'
        db.add_column('oxero_itinerary', 'width',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Itinerary.height'
        db.add_column('oxero_itinerary', 'height',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Itinerary.map'
        db.add_column('oxero_itinerary', 'map',
                      self.gf('stdimage.fields.StdImageField')(thumbnail_size={'width': 273, 'force': True, 'height': 150}, upload_to='uploaded_images/%Y/%m/%d', max_length=255, blank=True, null=True, size={'width': 472, 'force': True, 'height': 306}),
                      keep_default=False)


        # Changing field 'SiteActivity.image'
        db.alter_column('oxero_siteactivity', 'image', self.gf('stdimage.fields.StdImageField')(max_length=255, null=True, upload_to='uploaded_images/%Y/%m/%d', size={'width': 183, 'force': True, 'height': 112}))
        # Adding field 'SiteHotel.width'
        db.add_column('oxero_sitehotel', 'width',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'SiteHotel.height'
        db.add_column('oxero_sitehotel', 'height',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'SiteHotel.map'
        db.add_column('oxero_sitehotel', 'map',
                      self.gf('stdimage.fields.StdImageField')(thumbnail_size={'width': 195, 'force': True, 'height': 150}, upload_to='uploaded_images/%Y/%m/%d', max_length=255, blank=True, null=True, size={'width': 453, 'force': True, 'height': 294}),
                      keep_default=False)


        # Changing field 'SiteImage.image'
        db.alter_column('oxero_siteimage', 'image', self.gf('stdimage.fields.StdImageField')(thumbnail_size={'width': 200, 'force': True, 'height': 148}, upload_to='uploaded_images/%Y/%m/%d', max_length=255, null=True, size={'width': 246, 'force': True, 'height': 160}))

    def backwards(self, orm):
        # Deleting field 'Itinerary.width'
        db.delete_column('oxero_itinerary', 'width')

        # Deleting field 'Itinerary.height'
        db.delete_column('oxero_itinerary', 'height')

        # Deleting field 'Itinerary.map'
        db.delete_column('oxero_itinerary', 'map')


        # Changing field 'SiteActivity.image'
        db.alter_column('oxero_siteactivity', 'image', self.gf('stdimage.fields.StdImageField')(size={'width': 246, 'force': True, 'height': 160}, upload_to='uploaded_images/%Y/%m/%d', max_length=255, null=True))
        # Deleting field 'SiteHotel.width'
        db.delete_column('oxero_sitehotel', 'width')

        # Deleting field 'SiteHotel.height'
        db.delete_column('oxero_sitehotel', 'height')

        # Deleting field 'SiteHotel.map'
        db.delete_column('oxero_sitehotel', 'map')


        # Changing field 'SiteImage.image'
        db.alter_column('oxero_siteimage', 'image', self.gf('stdimage.fields.StdImageField')(size={'width': 246, 'force': True, 'height': 160}, upload_to='uploaded_images/%Y/%m/%d', max_length=255, null=True))

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
            'description_en': ('django.db.models.fields.TextField', [], {}),
            'description_fr': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'height': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_example': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'last_active': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            'map': ('stdimage.fields.StdImageField', [], {'thumbnail_size': "{'width': 273, 'force': True, 'height': 150}", 'upload_to': "'uploaded_images/%Y/%m/%d'", 'max_length': '255', 'blank': 'True', 'null': 'True', 'size': "{'width': 472, 'force': True, 'height': 306}"}),
            'name_en': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'name_fr': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'sites': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['oxero.Site']", 'through': "orm['oxero.ItinerarySite']", 'symmetrical': 'False'}),
            'start_date': ('django.db.models.fields.DateField', [], {}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'width': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'oxero.itineraryimage': {
            'Meta': {'object_name': 'ItineraryImage'},
            'date': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'height': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('stdimage.fields.StdImageField', [], {'blank': 'True', 'max_length': '255', 'null': 'True', 'upload_to': "'uploaded_images/%Y/%m/%d'", 'size': "{'width': 246, 'force': True, 'height': 160}"}),
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
            'hotel': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['oxero.SiteHotel']", 'null': 'True', 'blank': 'True'}),
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
            'description_en': ('django.db.models.fields.TextField', [], {}),
            'description_fr': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'do_not_miss_en': ('django.db.models.fields.TextField', [], {}),
            'do_not_miss_fr': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'good_to_know_en': ('django.db.models.fields.TextField', [], {}),
            'good_to_know_fr': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'interests': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['oxero.Interest']", 'null': 'True', 'blank': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'last_active': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'price_en': ('django.db.models.fields.TextField', [], {}),
            'price_fr': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'rating': ('django.db.models.fields.IntegerField', [], {}),
            'recommended_stay_en': ('django.db.models.fields.TextField', [], {}),
            'recommended_stay_fr': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'region': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['oxero.Region']", 'null': 'True', 'blank': 'True'}),
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
            'image': ('stdimage.fields.StdImageField', [], {'blank': 'True', 'max_length': '255', 'null': 'True', 'upload_to': "'uploaded_images/%Y/%m/%d'", 'size': "{'width': 183, 'force': True, 'height': 112}"}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'last_active': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name_en': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'name_fr': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['oxero.Site']"}),
            'width': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'oxero.sitehotel': {
            'Meta': {'object_name': 'SiteHotel'},
            'date': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description_en': ('django.db.models.fields.TextField', [], {}),
            'description_fr': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'height': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'last_active': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            'map': ('stdimage.fields.StdImageField', [], {'thumbnail_size': "{'width': 195, 'force': True, 'height': 150}", 'upload_to': "'uploaded_images/%Y/%m/%d'", 'max_length': '255', 'blank': 'True', 'null': 'True', 'size': "{'width': 453, 'force': True, 'height': 294}"}),
            'name_en': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'name_fr': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'price': ('django.db.models.fields.FloatField', [], {}),
            'width': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
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