#!/usr/bin/python
# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import unittest
import time


class Test1(unittest.TestCase):
    def test_2(self):
        self.driver = webdriver.Firefox()
        self.driver.set_window_size(1920, 1080)
        self.driver.implicitly_wait(30)
        driver = self.driver
        driver.get("http://blog.csssr.ru/qa-engineer/")

        # scroll page
        graphs = driver.find_element_by_class_name("graphs")
        driver.execute_script("arguments[0].scrollIntoView()", graphs)
        time.sleep(5)

        # double click to element
        tab = driver.find_element_by_css_selector(".graphs-errors>a")
        ActionChains(driver).move_to_element(tab).double_click().perform()
        time.sleep(3)

        # create screenshot
        driver.save_screenshot('DoubleClickToTab.png')

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
