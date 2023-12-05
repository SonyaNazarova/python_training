from model.contact import Contact


def test_modify_first_contact_firstname(app):
    app.session.loqin(username="admin", password="secret")
    app.contact.modify_first_contact(Contact(firstname="firstname"))
    app.session.logout()