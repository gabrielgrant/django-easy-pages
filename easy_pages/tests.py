from django.test import TestCase

from .models import PageManager, Page

class PageManagerTests(TestCase):
	def setUp(self):
		self.pm = PageManager()
	def test_path2query(self):
		q = self.pm.path2query('/this/is/a/path')
		self.assertEqual(q, {
			'parent__parent__parent__slug': 'this',
			'parent__parent__slug': 'is',
			'parent__slug': 'a',
			'slug': 'path',
			'parent__parent__parent__parent': None,
		})
	def test_root_path2query(self):
		q = self.pm.path2query('/ThisIsAPathToo/')
		self.assertEqual(q['slug'], 'ThisIsAPathToo')
		self.assertEqual(q['parent'], None)
