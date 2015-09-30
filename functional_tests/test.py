from django.test import LiveServerTestCase
# the above must have unit test in it
from selenium import webdriver

#allows ENTER instead of \n
from selenium.webdriver.common.keys import Keys

class NewVisitorTest(LiveServerTestCase):
	def setUp(self): 
		self.browser = webdriver.Firefox()
	
	def tearDown(self):
		self.browser.quit()

	#helper method - DRY
	def check_for_row_in_list_table(self, rowtext):
		table = self.browser.find_element_by_id('id_list_table')
		rows = table.find_elements_by_tag_name('tr')
		self.assertIn( rowtext,  [row.text for row in rows])

	def enter_an_item_in_list_table(self, itemToEnter):
		inputBox = self.browser.find_element_by_id('id_new_item')
		self.assertEqual(inputBox.get_attribute('placeholder'), 'Enter a To-Do item')
		inputBox.send_keys(itemToEnter)
		inputBox.send_keys('\n')

	
	def test_home_page(self):
		# Edith has heard about a ool new online to-do app. She goes to 
		# check out its home page
		self.browser.get(self.live_server_url)
	
		#she notices the page title and header mention to-do lists.. 	
		self.assertIn( 'To-Do', self.browser.title)
		header = self.browser.find_element_by_tag_name('h1')
		self.assertIn('To-Do', header.text)

		# She is invited to enter a to-do item straight away
		# She types "Buy peacock feathers" into a text box (Edith's hobby
		# is tying fly-fishing lures)
		self.enter_an_item_in_list_table('Buy peacock feathers')

		# When she hits enter, the page updates, and now the page lists
		# "1: Buy peacock feathers" as an item in a to-do list
		self.check_for_row_in_list_table("1: Buy peacock feathers")

		# There is still a text box inviting her to add another item. She
		# enters "Use peacock feathers to make a fly" (Edith is very methodical)
		self.enter_an_item_in_list_table('Use peacock feathers to make a fly')

		# The page updates again, and now shows both items on her list
		self.check_for_row_in_list_table("1: Buy peacock feathers")
		self.check_for_row_in_list_table('2: Use peacock feathers to make a fly')
		
		# Edith wonders whether the site will remember her list. Then she sees
		# that the site has generated a unique URL for her -- there is some
		# explanatory text to that effect.

		#PAUSES PROGRAM FOR 10 SECONDS 
		import time
		time.sleep(5)
		self.fail('finish the test!')#havent finished coding

		# She visits that URL - her to-do list is still there.
		# Satisfied, she goes back to sleep
		
