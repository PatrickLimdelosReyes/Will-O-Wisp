from selenium import webdriver
import unittest
from .views import HomeView

class NewVisitorTest(unittest.TestCase):
	def setUp(self):
		self.browser = webdriver.Firefox()
		#self.browser.implicitly_wait(30)
		
	def tearDown(self):
		self.browser.quit()

	def test_can_display_a_heroes_list_and_more_information_per_hero(self):
		# Widget has heard about a new wiki app for the game called The Will of the Wisps. 
		# She goes to check out its homepage
		self.browser.get('http://localhost:8000')

		# She notices the page title and header mention 
		# 'The Will of the Wisps Wiki'
		self.assertIn('The Will of the Wisps Wiki', self.browser.title)
		
		# She sees a list containing three heroes with their corresponding 
		# names, health points, and damage 
		detail = self.browser.find_element_by_id('cloudName')
		self.assertEqual(detail.get_attribute('innerHTML'), 'Cloud')
		detail = self.browser.find_element_by_id('cloudHealth')
		self.assertEqual(detail.get_attribute('innerHTML'), '600')
		detail = self.browser.find_element_by_id('cloudAttack')
		self.assertEqual(detail.get_attribute('innerHTML'), '57')
		
		detail = self.browser.find_element_by_id('jesterName')
		self.assertEqual(detail.get_attribute('innerHTML'), 'Jester')
		detail = self.browser.find_element_by_id('jesterHealth')
		self.assertEqual(detail.get_attribute('innerHTML'), '660')
		detail = self.browser.find_element_by_id('jesterAttack')
		self.assertEqual(detail.get_attribute('innerHTML'), '64')
		
		detail = self.browser.find_element_by_id('sunName')
		self.assertEqual(detail.get_attribute('innerHTML'), 'Sunflowey')
		detail = self.browser.find_element_by_id('sunHealth')
		self.assertEqual(detail.get_attribute('innerHTML'), '650')
		detail = self.browser.find_element_by_id('sunAttack')
		self.assertEqual(detail.get_attribute('innerHTML'), '43')
		
		# When she selects one of the heroes, she is sent to another page
		# containing more information about the hero (additional stats, lore, image).
		self.browser.get('http://localhost:8000/hero/cloud')
		
		# She spots the page title and header mentions the name of the hero she selected.
		detail = self.browser.find_element_by_id('cloudtitle')
		self.assertEqual(detail.get_attribute('innerHTML'), 'Detail - Cloud')
		detail = self.browser.find_element_by_id('cloudheading')
		self.assertEqual(detail.get_attribute('innerHTML'), 'Detail - Cloud')
		
		# While she is in a specific hero's page, she sees a button labeled "Back to Heroes List".
		# She clicks this and she is redirected back to the wiki's homepage.
		button = self.browser.find_element_by_id('button').click()		
		
		#self.assertEqual(resolve('/').func, home)
		self.fail('Finish the test!')
		
if __name__ == '__main__':
	unittest.main(warnings='ignore')