from django import template
from easy_pages.models import Page

register = template.Library()

@register.inclusion_tag('easy_pages/page_menu.html')
def page_menu(page):
	if page and not isinstance(page, Page):
		try:
			page = Page.objects.page_or_ancestor_from_path(page)
		except Page.DoesNotExist:
			page = None
	return {'page': page}

@register.inclusion_tag('easy_pages/main_menu.html')
def main_menu(depth, page=None):
	if not isinstance(page, Page) and page is not None:
		page = '/'.join(page.rstrip('/').split('/')[:depth+1])
		try:
			page = Page.objects.from_path(page)
		except Page.DoesNotExist:
			page = None
	return {'page': page, 'roots': Page.tree.all(), 'depth':int(depth)}

