from setuptools import setup

setup(
    name='django-easy-pages',
    version='0.1.2',
    author='Gabriel Grant',
    packages=['easy_pages',],
    license='LGPL',
    long_description=open('README').read(),
    install_requires=[
        'django-mptt',
        'django-inline-edit',
        'django-ckeditor',
        'django-ckeditor-filemodel-manager',
        'django-html-field',
        'django-static-filtered-images',
        'django-python-identifier-field',
    ],
    dependency_links = [
    	'http://github.com/gabrielgrant/django-inline-edit/tarball/master#egg=django-inline-edit',
    	'http://github.com/gabrielgrant/django-ckeditor/tarball/master#egg=django-ckeditor',
    	'http://github.com/gabrielgrant/django-ckeditor-filemodel-manager/tarball/master#egg=django-ckeditor-filemodel-manager',
        'http://github.com/gabrielgrant/django-html-field/tarball/master#egg=django-html-field',
        'http://github.com/gabrielgrant/django-static-filtered-images/tarball/master#egg=django-static-filtered-images',
        'http://github.com/gabrielgrant/django-python-identifier-field/tarball/master#egg=django-python-identifier-field',
    ]
)

