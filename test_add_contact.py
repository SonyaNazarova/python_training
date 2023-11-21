# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest
from contact import Group

class TestAddContact(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    def open_home_paqe(self, wd):
        wd.get("http://localhost/addressbook/")


    def loqin(self, wd, username, password):
        wd.find_element("name", "user").clear()
        wd.find_element("name","user").send_keys(username)
        wd.find_element("name","pass").click()
        wd.find_element("name","pass").clear()
        wd.find_element("name","pass").send_keys(password)
        wd.find_element("xpath","//input[@value='Login']").click()


    def open_contact_page(self, wd):
        wd.find_element("link text", "add new").click()

    def create_contact(self, wd, contact):
        wd.find_element("name","firstname").click()
        wd.find_element("name","firstname").clear()
        wd.find_element("name","firstname").send_keys(contact.firstname)
        wd.find_element("name","middlename").click()
        wd.find_element("name","middlename").clear()
        wd.find_element("name","middlename").send_keys(contact.middlename)
        wd.find_element("name","lastname").click()
        wd.find_element("name","lastname").clear()
        wd.find_element("name","lastname").send_keys(contact.lastname)
        wd.find_element("name","nickname").click()
        wd.find_element("name","nickname").clear()
        wd.find_element("name","nickname").send_keys(contact.nickname)
        wd.find_element("name","title").click()
        wd.find_element("name","title").clear()
        wd.find_element("name","title").send_keys(contact.title)
        wd.find_element("name","company").click()
        wd.find_element("name","company").clear()
        wd.find_element("name","company").send_keys(contact.company)
        wd.find_element("name","address").click()
        wd.find_element("name","address").clear()
        wd.find_element("name","address").send_keys(contact.address)
        wd.find_element("name","home").click()
        wd.find_element("name","home").clear()
        wd.find_element("name","home").send_keys(contact.TelephoneHome)
        wd.find_element("name","mobile").click()
        wd.find_element("name","mobile").clear()
        wd.find_element("name","mobile").send_keys(contact.TelephoneMobile)
        wd.find_element("name","work").click()
        wd.find_element("name","work").clear()
        wd.find_element("name","work").send_keys(contact.TelephoneWork)
        wd.find_element("name","fax").click()
        wd.find_element("name","fax").clear()
        wd.find_element("name","fax").send_keys(contact.fax)
        wd.find_element("name","email").click()
        wd.find_element("name","email").clear()
        wd.find_element("name","email").send_keys(contact.email)
        wd.find_element("name","theform").click()
        wd.find_element("name","email2").click()
        wd.find_element("name","email2").clear()
        wd.find_element("name","email2").send_keys(contact.email2)
        wd.find_element("name","email3").click()
        wd.find_element("name","email3").clear()
        wd.find_element("name","email3").send_keys(contact.email3)
        wd.find_element("name","homepage").click()
        wd.find_element("name","homepage").clear()
        wd.find_element("name","homepage").send_keys(contact.homepage)
        wd.find_element("name","bday").click()
        Select(wd.find_element("name","bday")).select_by_visible_text(contact.bday)
        wd.find_element("name","bmonth").click()
        Select(wd.find_element("name","bmonth")).select_by_visible_text(contact.bmonth)
        wd.find_element("name","byear").click()
        wd.find_element("name","byear").clear()
        wd.find_element("name","byear").send_keys(contact.byear)
        wd.find_element("name","aday").click()
        Select(wd.find_element("name","aday")).select_by_visible_text(contact.aday)
        wd.find_element("name","amonth").click()
        Select(wd.find_element("name","amonth")).select_by_visible_text(contact.amonth)
        wd.find_element("name","ayear").click()
        wd.find_element("name","ayear").clear()
        wd.find_element("name","ayear").send_keys(contact.ayear)
        wd.find_element("name","theform").click()
        wd.find_element("name","address2").click()
        wd.find_element("name","address2").clear()
        wd.find_element("name","address2").send_keys(contact.address2)
        wd.find_element("name","phone2").click()
        wd.find_element("name","phone2").clear()
        wd.find_element("name","phone2").send_keys(contact.phone2)
        wd.find_element("name","notes").click()
        wd.find_element("name","notes").clear()
        wd.find_element("name","notes").send_keys(contact.notes)
        wd.find_element("xpath","//input[21]").click()


    def return_to_home(self, wd):
        wd.find_element("link text","home").click()


    def Logout(self, wd):
        wd.find_element("link text","Logout").click()
    
    def test_add_contact(self):
        wd = self.wd
        self.open_home_paqe(wd)
        self.loqin(wd, username="admin", password="secret")
        self.open_contact_page(wd)
        self.create_contact(wd, Group(firstname="2",middlename="1", lastname="3", nickname="4", title="5", address="7", company="6", TelephoneHome="8", TelephoneMobile="9",
                            TelephoneWork="10", fax="11", email="12", email2="13", email3="14", homepage="15", bday="9",
                            bmonth="January", byear="1988", aday="14", amonth="February", ayear="2000", address2="16", phone2="17", notes="18"))
        self.return_to_home(wd)
        self.Logout(wd)



    def is_element_present(self, how, what):
        try: self.wd.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.wd.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True

    
    def tearDown(self):
        self.wd.quit()


if __name__ == "__main__":
    unittest.main()
