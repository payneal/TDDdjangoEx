from django.test import TestCase
#from django.http import HttpRequest

#from lists.views import home_page

# Create your tests here.

class HomePageViewTest(TestCase): 

	def test_home_page_returns_correct_html(self):
		self.assertEqual(1+1, 3)
		#request = HttpRequest()
		#response = home_page(request)
		#self.assertIn('<title> To-Do lists </title>', response.content)
		
