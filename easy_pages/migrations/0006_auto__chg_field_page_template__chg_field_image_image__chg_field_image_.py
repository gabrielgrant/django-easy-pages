# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Changing field 'Page.template'
        db.alter_column('easy_pages_page', 'template', self.gf('django.db.models.fields.FilePathField')(path='/home/gabriel/Documents/alton_mill/alton-mill/alton_mill/settings/../templates/easy_pages', max_length=200, match='.*\\.html$'))

        # Changing field 'Image.image'
        db.alter_column('easy_pages_image', 'image', self.gf('django.db.models.fields.files.ImageField')(max_length=200))

        # Changing field 'Image.display_image'
        db.alter_column('easy_pages_image', 'display_image', self.gf('static_filtered_images.fields.FilteredImageField')(no_old_src_field=True, max_length=200))


    def backwards(self, orm):
        
        # Changing field 'Page.template'
        db.alter_column('easy_pages_page', 'template', self.gf('django.db.models.fields.FilePathField')(path='/home/gabriel/Documents/alton mill/site2/alton_mill/settings/../templates/easy_pages', max_length=200, match='.*\\.html$'))

        # Changing field 'Image.image'
        db.alter_column('easy_pages_image', 'image', self.gf('django.db.models.fields.files.ImageField')(max_length=100))

        # Changing field 'Image.display_image'
        db.alter_column('easy_pages_image', 'display_image', self.gf('static_filtered_images.fields.FilteredImageField')(no_old_src_field=True, max_length=100))


    models = {
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'easy_pages.contentblock': {
            'Meta': {'ordering': "('_order',)", 'unique_together': "(('name', 'page'),)", 'object_name': 'ContentBlock'},
            '_html_content_cache': ('django.db.models.fields.TextField', [], {'default': "''"}),
            '_order': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'block_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['easy_pages.ContentBlockType']"}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']", 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('python_identifier_field.db.models.fields.PythonIdentifierField', [], {'max_length': '50', 'db_index': 'True'}),
            'page': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'content_blocks'", 'to': "orm['easy_pages.Page']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'})
        },
        'easy_pages.contentblocktype': {
            'Meta': {'object_name': 'ContentBlockType'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('python_identifier_field.db.models.fields.PythonIdentifierField', [], {'unique': 'True', 'max_length': '50', 'db_index': 'True'})
        },
        'easy_pages.image': {
            'Meta': {'object_name': 'Image'},
            '_old_image_source_for_display_image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'caption': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'content_block': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'images'", 'to': "orm['easy_pages.ContentBlock']"}),
            'credit': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'display_image': ('static_filtered_images.fields.FilteredImageField', [], {'no_old_src_field': 'True', 'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '200'})
        },
        'easy_pages.page': {
            'Meta': {'unique_together': "(('slug', 'parent'),)", 'object_name': 'Page'},
            'changefreq': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lastmod': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'page_type': ('django.db.models.fields.CharField', [], {'default': "'norm'", 'max_length': '4'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'children'", 'null': 'True', 'to': "orm['easy_pages.Page']"}),
            'priority': ('django.db.models.fields.FloatField', [], {'default': '0.5', 'blank': 'True'}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'show_in_menu': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'db_index': 'True'}),
            'template': ('django.db.models.fields.FilePathField', [], {'default': "''", 'path': "'/home/gabriel/Documents/alton_mill/alton-mill/alton_mill/settings/../templates/easy_pages'", 'max_length': '200', 'match': "'.*\\\\.html$'", 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'url_cache': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'})
        },
        'easy_pages.rawhtmlcontentblock': {
            'Meta': {'ordering': "('_order',)", 'object_name': 'RawHTMLContentBlock', '_ormbases': ['easy_pages.ContentBlock']},
            'content': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'contentblock_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['easy_pages.ContentBlock']", 'unique': 'True', 'primary_key': 'True'})
        },
        'easy_pages.restrictedhtmlcontentblock': {
            'Meta': {'ordering': "('_order',)", 'object_name': 'RestrictedHTMLContentBlock', '_ormbases': ['easy_pages.ContentBlock']},
            'content': ('html_field.db.models.fields.HTMLField', [], {'blank': 'True'}),
            'contentblock_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['easy_pages.ContentBlock']", 'unique': 'True', 'primary_key': 'True'})
        }
    }

    complete_apps = ['easy_pages']
