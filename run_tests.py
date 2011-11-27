
# from http://www.travisswicegood.com/2010/01/17/django-virtualenv-pip-and-fabric/
import os

from django.conf import settings
from django.core.management import call_command
import easy_pages

def main():
    # Dynamically configure the Django settings with the minimum necessary to
    # get Django running tests
    settings.configure(
        INSTALLED_APPS=(
            'django.contrib.auth',
            'django.contrib.contenttypes',
            'django.contrib.admin',
            'django.contrib.sessions',
            'django.contrib.sites',
            'easy_pages',
        ),
        # Django replaces this, but it still wants it. *shrugs*
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': '/tmp/django_test.db',
            }
        },
        MEDIA_ROOT = '/tmp/django_test_media/',
        ROOT_URLCONF = '',
        STATIC_URL = '/static/',
        DEBUG = True,
		TEMPLATE_DEBUG = True,
		TEMPLATE_DIRS = [
		    os.path.join(os.path.dirname(easy_pages.__file__), 'tests/templates')
		],
		SITE_ID = 1,
		PROJECT_ROOT = os.path.dirname(__file__),
		EASY_PAGE_IMAGE_RESIZE = {'width':280, 'style':"=="},
    ) 
    
    #call_command('syncdb')
    
    # Fire off the tests
    call_command('test', 'easy_pages')
    

if __name__ == '__main__':
    main()

