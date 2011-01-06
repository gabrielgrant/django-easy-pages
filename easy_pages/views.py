from easy_pages.models import Page
from django.template import loader, RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.core.xheaders import populate_xheaders

DEFAULT_TEMPLATE = 'easy_pages/default.html'
def easy_page(request, page):
	"""
	Easy Page view.

	Models: `easy_pages.models.Page`
	Templates: Uses the template defined by the ``template_name`` field,
	    or `simple_pages/default.html` if template_name is not defined.
	Context:
	    page
	        `easy_pages.models.Page` object
	"""
	if page.template:
		#template_name = 'templates/'.join(page.template.split('templates/')[1:])
		t = loader.select_template((page.template, DEFAULT_TEMPLATE))
	else:
		t = loader.get_template(DEFAULT_TEMPLATE)

	c = RequestContext(request, {
	    'page': page,
	})
	response = HttpResponse(t.render(c))
	populate_xheaders(request, response, Page, page.id)
	return response
