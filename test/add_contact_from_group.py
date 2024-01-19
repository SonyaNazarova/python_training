from model.contact import Contact
from model.group import Group
import random



def test_add_contact_from_group(app, db):
    old_contacts = db.get_contact_list()
    old_groups = db.get_group_list()
    if len(old_contacts) == 0:
        app.contact.create(Contact(firstname="test"))
        old_contacts = db.get_contact_list()
    if len(old_groups) == 0:
        app.group.create(Group(name="test"))
        old_groups = db.get_group_list()
    new_groups = random.choice(old_groups)
    new_contacts = random.choice(old_contacts)
    #if db.all_contacts_are_in_all_groups():
     #  app.contact.create(Contact(firstname="test"))
      # new_contacts = db.get_contact_list()
    if new_contacts in db.get_contacts_in_group(new_groups):
        app.contact.create(Contact(firstname="test"))
        new_contacts = db.get_contact_list()[-1]
    app.contact.select_group(new_contacts.id, new_groups.id)
    contacts_in_group = db.get_contacts_in_group((Group(id=new_groups.id)))
    assert  new_contacts  in  contacts_in_group