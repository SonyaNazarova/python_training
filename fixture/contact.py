from selenium.webdriver.support.ui import Select
from model.contact import Contact
import re

class ContactHelper:

    def __init__(self, app):
        self.app = app

    def open_contact_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/addressbook/") and len(wd.find_elements("name", "Select all")) > 0):
            wd.find_element("link text", "add new").click()


    def create(self, contact):
        wd = self.app.wd
        self.open_contact_page()
        self.fill_contact_form(contact)
        wd.find_element("xpath", "//input[21]").click()
        self.return_to_home()
        self.contact_cache = None

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("middlename", contact.middlename)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("nickname", contact.nickname)
        self.change_field_value("title", contact.title)
        self.change_field_value("company", contact.company)
        self.change_field_value("address", contact.address)
        self.change_field_value("home", contact.telephone_home)
        self.change_field_value("mobile", contact.telephone_mobile)
        self.change_field_value("work", contact.telephone_work)
        self.change_field_value("fax", contact.fax)
        self.change_field_value("email", contact.email)
        self.change_field_value("email2", contact.email2)
        self.change_field_value("email3", contact.email3)
        self.change_field_value("homepage", contact.homepage)
        self.select_field_value("bday", contact.bday)
        self.select_field_value("bmonth", contact.bmonth)
        self.change_field_value("byear", contact.byear)
        self.select_field_value("aday", contact.aday)
        self.select_field_value("amonth", contact.amonth)
        self.change_field_value("ayear", contact.ayear)
        self.change_field_value("address2", contact.address2)
        self.change_field_value("phone2", contact.phone2)
        self.change_field_value("notes", contact.notes)

    def select_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element("name", field_name).click()
            Select(wd.find_element("name", field_name)).select_by_visible_text(text)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element("name", field_name).click()
            wd.find_element("name", field_name).clear()
            wd.find_element("name", field_name).send_keys(text)

    def return_to_home(self):
        wd = self.app.wd
        wd.find_element("link text", "home").click()

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.return_to_home()
        self.select_contact_by_index(index)
        # select first contact
        wd.find_element("name", "selected[]").click()
        # submit deletion
        wd.find_element("xpath", "//input[@value='Delete']").click()
        wd.switch_to.alert.accept()
        self.return_to_home()
        self.contact_cache = None


    def delete_contact_by_id(self, id):
        wd = self.app.wd
        self.return_to_home()
        self.select_contact_by_id(id)
        # select first contact
        #wd.find_element("name", "selected[]").click()
        # submit deletion
        wd.find_element("xpath", "//input[@value='Delete']").click()
        self.return_to_home()
        self.contact_cache = None

    def modify_first_contact(self, new_contact_data):
        self.modify_contact_by_index(0)



    def modify_contact_by_index(self, index, new_contact_data):
        wd = self.app.wd
        self.return_to_home()
        self.select_contact_by_index(index)
        # open modification form
        wd.find_elements("xpath", "//img[@alt='Edit']")[index].click()
        #edit
        self.fill_contact_form(new_contact_data)
        # submit group edit
        wd.find_element("xpath", "//input[22]").click()
        self.return_to_home()
        self.contact_cache = None

    def modify_contact_by_id(self, id, new_contact_data):
        wd = self.app.wd
        self.return_to_home()
        self.select_contact_by_id(id)
        # open modification form
        self.fill_contact_form(new_contact_data)
        wd.find_element("xpath", "//input[@value='Update']").click()
        self.return_to_home()
        self.contact_cache = None

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements("name", "selected[]")[index].click()


    def select_contact_by_id(self, id):
        wd = self.app.wd
        self.return_to_home()
        wd.find_element("css selector", "input[value='%s']" % id).click()
        wd.find_element("css selector", "a[href='edit.php?id=%s']" % id).click()

    def count(self):
        wd = self.app.wd
        self.return_to_home()
        return len(wd.find_elements("name", "selected[]"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.return_to_home()
            self.contact_cache = []
            for element in wd.find_elements("xpath", "//tr[@name='entry']"):
                id = element.find_element("name", "selected[]").get_attribute("value")
                firstname = element.find_element("xpath", ".//td[3]").text
                lastname = element.find_element("xpath", ".//td[2]").text
                all_phones = element.find_element("xpath", ".//td[6]").text
                address = element.find_element("xpath", ".//td[4]").text
                all_emails = element.find_element("xpath", ".//td[5]").text
                self.contact_cache.append(Contact(firstname=firstname, lastname=lastname, id=id,
                                                  all_phones_from_home_page=all_phones, address=address, all_emails=all_emails))

        return list(self.contact_cache)


    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.return_to_home()
        wd.find_elements("name", "selected[]")[index].click()
        wd.find_elements("xpath", "//img[@title='Details']")[index].click()

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.return_to_home()
        wd.find_elements("name", "selected[]")[index].click()
        wd.find_elements("xpath", "//img[@title='Edit']")[index].click()


    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        firstname = wd.find_element("name", "firstname").get_attribute("value")
        lastname = wd.find_element("name", "lastname").get_attribute("value")
        id = wd.find_element("name", "id").get_attribute("value")
        telephone_home = wd.find_element("name", "home").get_attribute("value")
        telephone_mobile = wd.find_element("name", "mobile").get_attribute("value")
        telephone_work = wd.find_element("name", "work").get_attribute("value")
        phone2 = wd.find_element("name", "phone2").get_attribute("value")
        address = wd.find_element("name", "address").get_attribute("value")
        email = wd.find_element("name", "email").get_attribute("value")
        email2 = wd.find_element("name", "email2").get_attribute("value")
        email3 = wd.find_element("name", "email3").get_attribute("value")
        return Contact(firstname=firstname, lastname=lastname, id=id,
                    telephone_home=telephone_home, telephone_mobile=telephone_mobile,
                    telephone_work=telephone_work, phone2=phone2, address=address,
                       email=email, email2=email2, email3=email3)


    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element("id", "content").text
        telephone_home = re.search("H: (.*)", text).group(1)
        telephone_work = re.search("W: (.*)", text).group(1)
        telephone_mobile = re.search("M: (.*)", text).group(1)
        return Contact(telephone_home=telephone_home, telephone_mobile=telephone_mobile,
                    telephone_work=telephone_work)



