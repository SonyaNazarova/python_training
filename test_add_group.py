# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest


class test_add_group2(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)


    def open_home_paqe(self, wd):
        wd.get("http://localhost/addressbook/")


    def loqin(self, wd, username, password):
        wd.find_element("name", "user").clear()
        wd.find_element("name", "user").send_keys(username)
        wd.find_element("name", "pass").click()
        wd.find_element("name", "pass").clear()
        wd.find_element("name", "pass").send_keys(password)
        wd.find_element("xpath", "//input[@value='Login']").click()


    def open_groups_page(self, wd):
        wd.find_element("link text", "groups").click()


    def create_group(self, wd, name, header, footer):
        # init group creation
        wd.find_element("name", "new").click()
        # fill group form
        wd.find_element("name", "group_name").click()
        wd.find_element("name", "group_name").clear()
        wd.find_element("name", "group_name").send_keys(name)
        wd.find_element("name", "group_header").click()
        wd.find_element("name", "group_header").clear()
        wd.find_element("name", "group_header").send_keys(header)
        wd.find_element("name", "group_footer").click()
        wd.find_element("name", "group_footer").clear()
        wd.find_element("name", "group_footer").send_keys(footer)
        # submit group creation
        wd.find_element("name", "submit").click()


    def return_to_group_page(self, wd):
        wd.find_element("link text", "group page").click()


    def logout(self, wd):
        wd.find_element("link text", "Logout").click()

    def test_add_group2(self):
        wd = self.wd
        self.open_home_paqe(wd)
        self.loqin(wd, username="admin", password="secret")
        self.open_groups_page(wd)
        self.create_group(wd, name="2", header="234", footer="2345")
        self.return_to_group_page(wd)
        self.logout(wd)


    def test_add_empty_group2(self):
        wd = self.wd
        self.open_home_paqe(wd)
        self.loqin(wd, username="admin", password="secret")
        self.open_groups_page(wd)
        self.create_group(wd, name="", header="", footer="")
        self.return_to_group_page(wd)
        self.logout(wd)

    def is_element_present(self, how, what):
        try:
            self.wd.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True
    def is_alert_present(self):
        try:
            self.wd.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True
    def tearDown(self):
        self.wd.quit()
if __name__ == "__main__":
    unittest.main()