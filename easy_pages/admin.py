from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from easy_pages.models import Page

class PageAdmin(MPTTModelAdmin):
	prepopulated_fields = {"slug": ("title",)}
	fieldsets = [
		(None, {'fields':['title', 'slug', 'page_type', 'parent', 'published', 'show_in_menu']}),
		('Advanced Options', {'fields':['template'], 'classes':['collapse']}),
		('Sitemap information', {'fields': ['changefreq','priority'], 'classes':['collapse']}),
	]

admin.site.register(Page, PageAdmin)

