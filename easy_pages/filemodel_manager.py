import ckeditor_filemodel_manager as manager

from easy_pages.models import RestrictedHTMLContentBlock, Image

class CBManager(manager.ModelManager):
	image_set_fieldname = 'images'
	image_fieldname = 'display_image'

manager.site.register(RestrictedHTMLContentBlock, 'content', CBManager, use_ckeditor_formfield=True)
#)
