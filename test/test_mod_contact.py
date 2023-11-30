from model.contact import Group


def test_mod_first_contact(app):
    app.session.loqin(username="admin", password="secret")
    app.contact.mod_first_contact (Group(firstname="888"))
    app.session.logout()