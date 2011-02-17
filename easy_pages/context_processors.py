from easy_pages.models import Page

def page(request):
	""" returns the Page for the current request (if it exists)"""
	try:
		return {'page': Page.objects.from_path(request.path_info)}
	except Page.DoesNotExist:
		return {'page': None}
