from django.db import models
from django.conf import settings
from django.utils.safestring import mark_safe
from django.contrib.contenttypes.models import ContentType

from mptt.models import MPTTModel

from python_identifier_field.db.models import PythonIdentifierField

from static_filtered_images.fields import FilteredImageField
from static_filtered_images.image_filters import  \
	ResizeFilter, TextWatermarkFilter

class PageManager(models.Manager):
	def from_path(self, path):
		num_path_list = enumerate(reversed(path.strip('/').split('/')))
		query = dict((('parent__'*i)+'slug', slug) for i, slug in num_path_list)
		return self.model.objects.get(**query)

class Page(MPTTModel):
	objects = PageManager()
	
	PAGE_CHOICES = (
	  ('norm', 'Normal Page with content'),
	  ('link', 'Link only (no content)'),  # enter link in content field if different from slug-based path
	  ('cat', 'Category only (no link)'),  # content field is ignored
	)
	
	title = models.CharField(max_length=128)
	slug = models.SlugField()
	parent = models.ForeignKey('self', related_name='children')
	published = models.BooleanField(default=False)
	show_in_menu = models.BooleanField(default=True)
	page_type = models.CharField(max_length=4, choices=PAGE_CHOICES, default='norm')
	template = models.FilePathField(path='./templates/easy_pages', match='.*\.html$', blank=True, default='')
	# the following attributes are for sitemap integration:
	
	CHANGEFREQ_CHOICES = (
	  ('a', 'always'),
      ('h', 'hourly'),
      ('d', 'daily'),
      ('w', 'weekly'),
      ('m', 'monthly'),
      ('y', 'yearly'),
      ('n', 'never'),
    )
	
	changefreq = models.CharField(max_length=1, choices=CHANGEFREQ_CHOICES, blank=True)
	priority = models.FloatField(default=0.5, blank=True)
	lastmod = models.DateTimeField(auto_now=True)
	
	def __unicode__(self):
		return u"%s -- %s" % (self.get_absolute_url(), self.title)
	
	class Meta:
		unique_together = ('slug', 'parent')

	def get_absolute_url(self):
		u = '/'+'/'.join(i.slug for i in self.get_ancestors())
		if not u.endswith('/') and settings.APPEND_SLASH:
			return '%s/' % u
		else:
			return u

	@property
	def blocks(self):
		return BlocksAttr(self)
	@property
	def block(self):
		return BlockAttr(self)

	@property
	def content(self):
		try:
			return self.block.main.content
		except ContentBlock.DoesNotExist:
			return ''

class BlocksAttr(object):
	def __init__(self, instance):
		self._instance = instance
	def __getattr__(self, name):
		return self._instance.content_blocks.filter(block_type__name=name)

class BlockAttr(object):
	def __init__(self, instance):
		self._instance = instance
	def __getattr__(self, name):
		return self._instance.content_blocks.get(name=name)

class ContentBlock(models.Model):
	"""
	ContentBlock should be subclassed to implement specific types of content
	
	subclasses must implement a "content_as_html" method, which returns the
	content as an html.
	
	The convention is to store (possibly raw) content in a "content" field,
	but this isn't mandatory -- the content can be generated in any way
	
	"""
	title = models.CharField(max_length=128, blank=True)
	name = PythonIdentifierField()
	page = models.ForeignKey('Page', related_name='content_blocks')
	block_type = models.ForeignKey('ContentBlockType')
	content_type = models.ForeignKey(ContentType, editable=False, null=True)
	_html_content_cache = models.TextField(editable=False)

	def save(self):
		if not self.content_type:
			if self.__class__ is ContentBlock:
				raise RuntimeError('ContentBlock must be subclassed')
			self.content_type = ContentType.objects.get_for_model(self.__class__)
		# clear cached HTML content
		self._html_content_cache = ''
		super(ContentBlock, self).save()

	def content_as_html(self):
		if self._html_content_cache == '':
			# cache is empty: get the subclass to generate the content
			model = self.content_type.model_class()
			if(model == ContentBlock):
				raise RuntimeError('ContentBlock must be subclassed')
			obj = model.objects.get(id=self.id)
			self._html_content_cache = obj.content_as_html()
		return mark_safe(self._html_content_cache)
	
	def __unicode__(self):
		if self.title:
			return u'%s -- %s ("%s")' % (self.page.title, self.name, self.title)
		else:
			return u'%s -- %s' % (self.page.title, self.name)
	
	class Meta:
		unique_together = ('name', 'page')
		order_with_respect_to = 'page'

class ContentBlockType(models.Model):
	name = PythonIdentifierField(unique=True)
	
	def __unicode__(self):
		return self.name

def img_location(instance, filename):
	return 'content_block_images/content_block_%d/%s'%(instance.content_block.id, basename(filename))

class Image(models.Model):
	content_block = models.ForeignKey('ContentBlock', related_name='images')
	credit = models.CharField(max_length=200, blank=True)
	caption = models.TextField(blank=True)
	image = models.ImageField(upload_to=img_location)
	display_image = FilteredImageField(
		src_field=image,
		filter_chain=[
			ResizeFilter(**settings.EASY_PAGE_IMAGE_RESIZE),
			TextWatermarkFilter(field_name='credit')
		]
	)


##
#
#  Core ContentBlock Implementations
#
##
from html_field.db.models import HTMLField
from html_field import html_cleaner

default_cleaner = html_cleaner.HTMLCleaner(allow_tags=['h2', 'a', 'img', 'em', 'strong'])

html_cleaner = getattr(settings, 'EASY_PAGES_HTML_CLEANER', default_cleaner)

class RestrictedHTMLContentBlock(ContentBlock):
	content = HTMLField(html_cleaner, blank=True)
	def content_as_html(self):
		return self.content
	
class RawHTMLContentBlock(ContentBlock):
	content = models.TextField(blank=True)
	def content_as_html(self):
		return self.content
