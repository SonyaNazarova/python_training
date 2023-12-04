from model.contact import Group


def test_modify_first_contact_firstname(app):
    app.session.loqin(username="admin", password="secret")
    app.contact.modify_first_contact(Group(firstname="firstname"))
    app.session.logout()