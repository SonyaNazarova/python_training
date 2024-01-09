from model.contact import Contact
from model.group import Group
import random




def test_del_contact_from_group(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="test"))
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    old_contacts = db.get_contact_list()
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    if len(db.get_contacts_in_group(group.id)) == 0:
        new_contacts = random.choice(old_contacts)
        app.contact.select_group(new_contacts.id, group.id)
    contact = random.choice(db.get_contacts_in_group(group.id))
    app.contact.del_contact_from_group(contact.id, group.id)
    new_contact = db.get_contact_list()
    assert old_contacts == new_contact


