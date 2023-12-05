# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    app.contact.create(Contact(firstname="2", middlename="1", lastname="3", nickname="4", title="5", address="7", company="6", telephone_home="8", telephone_mobile="9",
                              telephone_work="10", fax="11", email="12", email2="13", email3="14", homepage="15", bday="9",
                              bmonth="January", byear="1988", aday="14", amonth="February", ayear="2000", address2="16", phone2="17", notes="18"))


def test_add_empty_contact(app):
    app.contact.create(Contact(firstname="", middlename="", lastname="", nickname="", title="", address="", company="", telephone_home="", telephone_mobile="",
                               telephone_work="", fax="", email="", email2="", email3="", homepage="", bday="",
                               bmonth="-", byear="", aday="", amonth="-", ayear="", address2="", phone2="", notes=""))