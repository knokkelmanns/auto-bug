#!/usr/bin/python
# -*- coding: utf-8 -*-
from selenium import webdriver
import unittest
import time


class Test3(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        #self.driver.set_window_size(1920, 1080)
        #self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.base_url = "http://blog.csssr.ru/qa-engineer/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_3(self):
        driver = self.driver
        driver.get(self.base_url)

        # choose tab
        driver.find_element_by_xpath("(//a[contains(@href, '#')])[3]").click()
        time.sleep(3)

        # scroll page
        graphs = driver.find_element_by_xpath(".//body/div[1]/section[1]/section/div[3]")
        driver.execute_script("arguments[0].scrollIntoView()", graphs)
        time.sleep(3)

        # create screenshot
        driver.save_screenshot('image/TestWrapping.png')


    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
