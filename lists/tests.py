from django.test import TestCase
from django.http import HttpRequest

from lists.views import home_page

# Create your tests here.

class HomePageViewTest(TestCase): 

	def test_home_page_returns_correct_html(self):
		request = HttpRequest()
		response = home_page(request)
		self.assertIn('<title>To-Do lists</title>', response.content.decode('UTF-8'))
		self.assertTrue(response.content.startswith(b'<html>'))
		self.assertTrue(response.content.endswith(b'</html>'))
		
