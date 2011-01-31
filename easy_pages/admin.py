from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from easy_pages.models import Page, Image, ContentBlock, ContentBlockType
from easy_pages.models import RestrictedHTMLContentBlock, RawHTMLContentBlock

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

class PageAdmin(MPTTModelAdmin):
	prepopulated_fields = {"slug": ("title",)}
	fieldsets = [
		(None, {'fields':['title', 'slug', 'page_type', 'parent', 'published', 'show_in_menu']}),
		('Advanced Options', {'fields':['template'], 'classes':['collapse']}),
		('Sitemap information', {'fields': ['changefreq','priority'], 'classes':['collapse']}),
	]
	inlines = [RestrictedHTMLContentBlockInline, RawHTMLContentBlockInline]

admin.site.register(Page, PageAdmin)

admin.site.register(Image)
admin.site.register(ContentBlockType)
admin.site.register(RestrictedHTMLContentBlock, ContentBlockAdmin)
admin.site.register(RawHTMLContentBlock, ContentBlockAdmin)
admin.site.register(ContentBlock, ContentBlockAdmin)
