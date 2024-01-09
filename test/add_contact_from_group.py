from model.contact import Contact
from model.group import Group
import random




def test_add_contact_from_group(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="test"))
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    old_contacts = db.get_contact_list()
    old_groups = db.get_group_list()
    new_groups = random.choice(old_groups)
    new_contacts = random.choice(old_contacts)
    app.contact.select_group(new_contacts.id, new_groups.id)
    new_contact = db.get_contact_list()
    assert old_contacts == new_contact
