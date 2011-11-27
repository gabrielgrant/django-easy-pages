from django.test import TestCase

from .models import PageManager, Page, ContentBlockType, RestrictedHTMLContentBlock

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

class PageGetAbsoluteURLTests(TestCase):
	def setUp(self):
		self.cbt = ContentBlockType.objects.create(name='main')
	def test_cat(self):
		p = Page.objects.create(title='category', slug='category', page_type='cat')
		self.assertEqual(p.get_absolute_url(), '')
	def test_link_oneword_content(self):
		p = Page.objects.create(title='oneword link', slug='oneword', page_type='link')
		cb = RestrictedHTMLContentBlock.objects.create(
			name='main', page=p, block_type=self.cbt, content='<p>alink</p>')
		self.assertEqual(p.get_absolute_url(), '/alink/')
	def test_link_many_words_content(self):
		p = Page.objects.create(title='manyword link', slug='manyword', page_type='link')
		cb = RestrictedHTMLContentBlock.objects.create(
			name='main', page=p, block_type=self.cbt, content='<p>this has many words</p>')
		self.assertEqual(p.get_absolute_url(), 'this has many words')
	def test_link_empty_content(self):
		p = Page.objects.create(title='empty link', slug='empty', page_type='link')
		cb = RestrictedHTMLContentBlock.objects.create(
			name='main', page=p, block_type=self.cbt, content='')
		self.assertEqual(p.get_absolute_url(), '')
	def test_link_oneword_content(self):
		p = Page.objects.create(title='oneword link', slug='norm', page_type='norm')
		cb = RestrictedHTMLContentBlock.objects.create(
			name='main', page=p, block_type=self.cbt, content='')
		self.assertEqual(p.get_absolute_url(), '/norm/')
