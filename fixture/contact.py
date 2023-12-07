from selenium.webdriver.support.ui import Select

class ContactHelper:

    def __init__(self, app):
        self.app = app

    def open_contact_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("http://localhost/addressbook/") and len(wd.find_elements("name", "Select all")) > 0):
            wd.find_element("link text", "add new").click()


    def create(self, contact):
        wd = self.app.wd
        self.open_contact_page()
        self.fill_contact_form(contact)
        wd.find_element("xpath", "//input[21]").click()
        self.return_to_home()

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
        wd = self.app.wd
        self.return_to_home()
        # select first contact
        wd.find_element("name", "selected[]").click()
        # submit deletion
        wd.find_element("xpath", "//input[@value='Delete']").click()
        wd.switch_to.alert.accept()
        self.return_to_home()

    def modify_first_contact(self, new_contact_data):
        wd = self.app.wd
        self.return_to_home()
        self.select_first_contact()
        # open modification form
        wd.find_element("xpath", "//img[@alt='Edit']").click()
        #edit
        self.fill_contact_form(new_contact_data)
        # submit group edit
        wd.find_element("xpath", "//input[22]").click()
        self.return_to_home()

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element("name", "selected[]").click()

    def count(self):
        wd = self.app.wd
        self.return_to_home()
        return len(wd.find_elements("name", "selected[]"))