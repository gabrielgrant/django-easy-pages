# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Page'
        db.create_table('easy_pages_page', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50, db_index=True)),
            ('parent', self.gf('django.db.models.fields.related.ForeignKey')(related_name='children', to=orm['easy_pages.Page'])),
            ('published', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('show_in_menu', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('page_type', self.gf('django.db.models.fields.CharField')(default='norm', max_length=4)),
            ('template', self.gf('django.db.models.fields.FilePathField')(default='', path='./templates/easy_pages', max_length=100, match='.*\\.html$', blank=True)),
            ('changefreq', self.gf('django.db.models.fields.CharField')(max_length=1, blank=True)),
            ('priority', self.gf('django.db.models.fields.FloatField')(default=0.5, blank=True)),
            ('lastmod', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('lft', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            ('rght', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            ('tree_id', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            ('level', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
        ))
        db.send_create_signal('easy_pages', ['Page'])

        # Adding unique constraint on 'Page', fields ['slug', 'parent']
        db.create_unique('easy_pages_page', ['slug', 'parent_id'])

        # Adding model 'ContentBlock'
        db.create_table('easy_pages_contentblock', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=128, blank=True)),
            ('name', self.gf('python_identifier_field.db.models.fields.PythonIdentifierField')(max_length=50)),
            ('page', self.gf('django.db.models.fields.related.ForeignKey')(related_name='content_blocks', to=orm['easy_pages.Page'])),
            ('block_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['easy_pages.ContentBlockType'])),
            ('content_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contenttypes.ContentType'], null=True)),
            ('_html_content_cache', self.gf('django.db.models.fields.TextField')()),
            ('_order', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal('easy_pages', ['ContentBlock'])

        # Adding unique constraint on 'ContentBlock', fields ['name', 'page']
        db.create_unique('easy_pages_contentblock', ['name', 'page_id'])

        # Adding model 'ContentBlockType'
        db.create_table('easy_pages_contentblocktype', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('python_identifier_field.db.models.fields.PythonIdentifierField')(unique=True, max_length=50)),
        ))
        db.send_create_signal('easy_pages', ['ContentBlockType'])

        # Adding model 'Image'
        db.create_table('easy_pages_image', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('content_block', self.gf('django.db.models.fields.related.ForeignKey')(related_name='images', to=orm['easy_pages.ContentBlock'])),
            ('credit', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('caption', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('display_image', self.gf('static_filtered_images.fields.FilteredImageField')(no_old_src_field=True, max_length=100)),
            ('_old_image_source_for_display_image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
        ))
        db.send_create_signal('easy_pages', ['Image'])


    def backwards(self, orm):
        
        # Removing unique constraint on 'ContentBlock', fields ['name', 'page']
        db.delete_unique('easy_pages_contentblock', ['name', 'page_id'])

        # Removing unique constraint on 'Page', fields ['slug', 'parent']
        db.delete_unique('easy_pages_page', ['slug', 'parent_id'])

        # Deleting model 'Page'
        db.delete_table('easy_pages_page')

        # Deleting model 'ContentBlock'
        db.delete_table('easy_pages_contentblock')

        # Deleting model 'ContentBlockType'
        db.delete_table('easy_pages_contentblocktype')

        # Deleting model 'Image'
        db.delete_table('easy_pages_image')


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
            '_html_content_cache': ('django.db.models.fields.TextField', [], {}),
            '_order': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'block_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['easy_pages.ContentBlockType']"}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']", 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('python_identifier_field.db.models.fields.PythonIdentifierField', [], {'max_length': '50'}),
            'page': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'content_blocks'", 'to': "orm['easy_pages.Page']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'})
        },
        'easy_pages.contentblocktype': {
            'Meta': {'object_name': 'ContentBlockType'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('python_identifier_field.db.models.fields.PythonIdentifierField', [], {'unique': 'True', 'max_length': '50'})
        },
        'easy_pages.image': {
            'Meta': {'object_name': 'Image'},
            '_old_image_source_for_display_image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'caption': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'content_block': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'images'", 'to': "orm['easy_pages.ContentBlock']"}),
            'credit': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'display_image': ('static_filtered_images.fields.FilteredImageField', [], {'no_old_src_field': 'True', 'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'})
        },
        'easy_pages.page': {
            'Meta': {'unique_together': "(('slug', 'parent'),)", 'object_name': 'Page'},
            'changefreq': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lastmod': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'page_type': ('django.db.models.fields.CharField', [], {'default': "'norm'", 'max_length': '4'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'children'", 'to': "orm['easy_pages.Page']"}),
            'priority': ('django.db.models.fields.FloatField', [], {'default': '0.5', 'blank': 'True'}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'show_in_menu': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'db_index': 'True'}),
            'template': ('django.db.models.fields.FilePathField', [], {'default': "''", 'path': "'./templates/easy_pages'", 'max_length': '100', 'match': "'.*\\\\.html$'", 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        }
    }

    complete_apps = ['easy_pages']
