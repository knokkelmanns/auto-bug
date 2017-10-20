#!/usr/bin/python
# -*- coding: utf-8 -*-
from selenium import webdriver
import unittest
import time


class Test2(unittest.TestCase):
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

        driver.find_element_by_xpath("(//a[contains(@href, '#')])[3]").click()

        driver.find_element_by_xpath(".//a[contains(text(), 'Умение рассуждать логически')]").click()
       # driver.find_element_by_xpath("//div[3]/aside/ul/li[3]/input").click()
      #  driver.find_element_by_xpath("//div[3]/aside/ul/li[2]/input").click()
       # driver.find_element_by_xpath("//div[3]/aside/ul/li/input").click()
        #driver.find_element_by_xpath("//div[3]/aside/ul/li[4]/input").click()
       # driver.find_element_by_xpath("//div[3]/aside/ul/li[3]/input").click()
        #driver.find_element_by_xpath("//div[3]/aside/ul/li[2]/input").click()
        #driver.find_element_by_xpath("//div[3]/aside/ul/li/input").click()
        time.sleep(10)

        # create screenshot
        driver.save_screenshot('CheckTheBox.png')

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()






