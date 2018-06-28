from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

broswer=webdriver.Firefox()

broswer.get('http://gabrielecirulli.github.io/2048/')
time.sleep(3)

htmlElement=broswer.find_element_by_tag_name('body')

while True:
	# htmlElement.send_keys(Keys.UP)
	# htmlElement.send_keys(Keys.RIGHT)
	# htmlElement.send_keys(Keys.DOWN)
	# htmlElement.send_keys(Keys.LEFT)

	htmlElement.send_keys(Keys.UP,Keys.RIGHT,Keys.DOWN,Keys.LEFT)

