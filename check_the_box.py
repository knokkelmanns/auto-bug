#!/usr/bin/python
# -*- coding: utf-8 -*-
from selenium import webdriver
import unittest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Test2(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.set_window_size(1920, 1080)
        self.driver.implicitly_wait(30)
        self.base_url = "http://blog.csssr.ru/qa-engineer/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_2(self):
        driver = self.driver
        driver.get(self.base_url)

        # choose tab
        driver.find_element_by_xpath("(//a[contains(@href, '#')])[3]").click()

        # scroll page
        graphs = driver.find_element_by_xpath(".//body/div[1]/section[2]/div[3]/aside/h3")
        driver.execute_script("arguments[0].scrollIntoView()", graphs)
        time.sleep(3)

        # unchecked checkbox
        wait = WebDriverWait(driver, 10)
        checkbox1 = wait.until(
            EC.presence_of_element_located((By.XPATH, ".//body/div[1]/section[2]/div[3]/aside/ul/li[1]/label")))
        checkbox2 = wait.until(
            EC.presence_of_element_located((By.XPATH, ".//body/div[1]/section[2]/div[3]/aside/ul/li[2]/label")))
        checkbox3 = wait.until(
            EC.presence_of_element_located((By.XPATH, ".//body/div[1]/section[2]/div[3]/aside/ul/li[3]/label")))
        checkbox4 = wait.until(
            EC.presence_of_element_located((By.XPATH, ".//body/div[1]/section[2]/div[3]/aside/ul/li[4]/label")))
        driver.execute_script("arguments[0].click();", checkbox1)
        driver.execute_script("arguments[0].click();", checkbox2)
        driver.execute_script("arguments[0].click();", checkbox3)
        driver.execute_script("arguments[0].click();", checkbox4)
        time.sleep(3)

        # create screenshot
        driver.save_screenshot('UnCheckTheBox.png')

        # checked checkbox
        wait = WebDriverWait(driver, 10)
        checkbox4 = wait.until(
            EC.presence_of_element_located((By.XPATH, ".//body/div[1]/section[2]/div[3]/aside/ul/li[4]/label")))
        checkbox3 = wait.until(
            EC.presence_of_element_located((By.XPATH, ".//body/div[1]/section[2]/div[3]/aside/ul/li[3]/label")))
        checkbox2 = wait.until(
            EC.presence_of_element_located((By.XPATH, ".//body/div[1]/section[2]/div[3]/aside/ul/li[2]/label")))
        checkbox1 = wait.until(
            EC.presence_of_element_located((By.XPATH, ".//body/div[1]/section[2]/div[3]/aside/ul/li[1]/label")))
        driver.execute_script("arguments[0].click();", checkbox4)
        driver.execute_script("arguments[0].click();", checkbox3)
        driver.execute_script("arguments[0].click();", checkbox2)
        driver.execute_script("arguments[0].click();", checkbox1)
        time.sleep(3)

        # create screenshot
        driver.save_screenshot('CheckTheBox.png')

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
