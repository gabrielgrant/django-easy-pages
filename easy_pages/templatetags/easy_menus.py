from django import template
from easy_pages.models import Page

register = template.Library()

@register.inclusion_tag('easy_pages/page_menu.html')
def page_menu(page):
	if type(page) is not Page:
		page = Page.objects.from_path(page)
	return {'page': page}

@register.inclusion_tag('easy_pages/main_menu.html')
def main_menu(depth, page=None):
	if type(page) is not Page and page is not None:
		page = '/'.join(page.strip('/').split('/')[:depth+1])
		page = Page.objects.from_path(page)
	return {'page': page, 'roots': Page.tree.root_nodes(), 'depth':int(depth)}

