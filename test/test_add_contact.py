# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="2", middlename="1", lastname="3", nickname="4", title="5", address="7", company="6", telephone_home="8", telephone_mobile="9",
                              telephone_work="10", fax="11", email="12", email2="13", email3="14", homepage="15", bday="9",
                              bmonth="January", byear="1988", aday="14", amonth="February", ayear="2000", address2="16", phone2="17", notes="18")
    app.contact.create(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


def test_add_empty_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="", middlename="", lastname="", nickname="", title="", address="", company="", telephone_home="", telephone_mobile="",
                                 telephone_work="", fax="", email="", email2="", email3="", homepage="", bday="",
                           bmonth="-", byear="", aday="", amonth="-", ayear="", address2="", phone2="", notes="")
    app.contact.create(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)