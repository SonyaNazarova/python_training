import re
from random import randrange


def test_contact(app, db):
    old_contacts = db.get_contact_list()
    for contact in old_contacts:
        assert contact.lastname == app.contact.get_contact_info_from_home_page_id(contact.id).lastname
        assert contact.firstname == app.contact.get_contact_info_from_home_page_id(contact.id).firstname
        assert contact.address == app.contact.get_contact_info_from_home_page_id(contact.id).address
        assert merge_phones_like_on_home_page(contact) == app.contact.get_contact_info_from_home_page_id(
            contact.id).all_phones_from_home_page
        assert merge_emails_on_home_page(contact) == app.contact.get_contact_info_from_home_page_id(
            contact.id).all_emails


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.telephone_home, contact.telephone_mobile, contact.telephone_work, contact.phone2]))))

def merge_emails_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "", [contact.email, contact.email2, contact.email3]))


def clear(s):
    return re.sub("[() -]","", s)

