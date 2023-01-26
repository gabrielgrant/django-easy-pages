from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from easy_pages.models import Page, Image, ContentBlock, ContentBlockType
from easy_pages.models import RestrictedHTMLContentBlock, RawHTMLContentBlock, ContentBlockLink

class ContentBlockLinkInline(admin.StackedInline):
	model = ContentBlockLink
	fields = ['url']

class ContentBlockAdmin(admin.ModelAdmin):
	prepopulated_fields = {"name": ("title",)}

class BaseContentBlockInline(admin.StackedInline):
	model = ContentBlock
	prepopulated_fields = ContentBlockAdmin.prepopulated_fields
	extra = 0

class RawHTMLContentBlockInline(BaseContentBlockInline):
	model = RawHTMLContentBlock

class RestrictedHTMLContentBlockInline(BaseContentBlockInline):
	model = RestrictedHTMLContentBlock
	fieldsets = [
		(None, {'fields':['title', 'content',]}),
		('Advanced Options',
			{'fields':['name', 'block_type'], 'classes':['collapse']}
		),
	]
	inlines = [ContentBlockLinkInline]

class PageAdmin(MPTTModelAdmin):
	prepopulated_fields = {"slug": ("title",)}
	fieldsets = [
		(None, {'fields':['title']}),
		('Advanced Options',
			{'fields':[
				'slug', 'page_type', 'parent',
				'template', 'published', 'show_in_menu'
			],
			'classes':['collapse']
		}),
		('Sitemap information',
		{'fields': ['changefreq','priority'], 'classes':['collapse']}),
	]
	inlines = [RestrictedHTMLContentBlockInline, RawHTMLContentBlockInline]
	save_on_top = True
	search_fields = ['title', 'slug']

admin.site.register(Page, PageAdmin)

admin.site.register(Image)
admin.site.register(ContentBlockType)
admin.site.register(RestrictedHTMLContentBlock, ContentBlockAdmin)
admin.site.register(RawHTMLContentBlock, ContentBlockAdmin)
admin.site.register(ContentBlock, ContentBlockAdmin)
