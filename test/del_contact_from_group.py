from model.contact import Contact
from model.group import Group
import random




def test_del_contact_from_group(app, db):
    old_groups = db.get_group_list()
    old_contacts = db.get_contact_list()
    if len(old_contacts) == 0:
        app.contact.create(Contact(firstname="test"))
        old_contacts = db.get_contact_list()
    if len(old_groups) == 0:
        app.group.create(Group(name="test"))
        old_groups = db.get_group_list()
    group = random.choice(old_groups)
    if len(db.get_contacts_in_group(group)) == 0:
        new_contacts = random.choice(old_contacts)
        app.contact.select_group(new_contacts.id, group.id)
    contact = random.choice(db.get_contacts_in_group(group))
    app.contact.del_contact_from_group(contact.id, group.id)
    contact_in_group = db.get_contacts_in_group(group)
    assert contact not in  contact_in_group