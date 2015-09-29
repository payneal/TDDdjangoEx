from django.test import TestCase
from django.http import HttpRequest
from django.template.loader import render_to_string

from lists.views import home_page

# Create your tests here.

class HomePageViewTest(TestCase): 

	def test_home_page_uses_home_template(self):
		request = HttpRequest()
		response = home_page(request)
		expected_content = render_to_string('home.html')
		self.assertEqual(response.content.decode('utf8'), expected_content)

	def test_home_page_can_store_post_request(self):
		request = HttpRequest()
		request.method = 'POST'
		request.POST['item_text'] = 'new item'
		response = home_page(request)
		expected_content = render_to_string('home.html', {'new_item_text': 'new item'})
		self.assertEqual(response.content.decode('utf8'), expected_content)

		

		
