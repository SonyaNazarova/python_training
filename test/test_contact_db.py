import random


def test_contact(app, db):
    old_contacts = db.get_contact_list()
    for contact in old_contacts:
        new_contacts = app.contact.get_contact_info_from_edit_page_id(contact.id)
        assert contact.lastname == new_contacts.lastname
        assert contact.firstname == new_contacts.firstname
        assert contact.address == new_contacts.address
        assert contact.telephone_home == new_contacts.telephone_home
        assert contact.telephone_mobile == new_contacts.telephone_mobile
        assert contact.telephone_work == new_contacts.telephone_work
        assert contact.phone2 == new_contacts.phone2
        assert contact.email == new_contacts.email
        assert contact.email2 == new_contacts.email2
        assert contact.email3 == new_contacts.email3


