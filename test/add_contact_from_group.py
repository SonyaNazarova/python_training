from model.contact import Contact
from model.group import Group
import random



def test_add_contact_from_group(app, db):
    old_contacts = db.get_contact_list()
    old_groups = db.get_group_list()
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="test"))
        old_contacts = db.get_contact_list()
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
        old_groups = db.get_group_list()
    new_groups = random.choice(old_groups)
    new_contacts = random.choice(old_contacts)
    if db.all_contacts_are_in_all_groups():
        app.group.create(Group(name="test"))
        new_groups = db.get_group_list()[-1]
    if new_contacts in db.get_contacts_in_group(new_groups):
        app.contact.del_contact_from_group(new_contacts.id, new_groups.id)
    app.contact.select_group(new_contacts.id, new_groups.id)
    contacts_in_group = db.get_contacts_in_group((Group(id=old_groups.id)))
    assert old_contacts == contacts_in_group