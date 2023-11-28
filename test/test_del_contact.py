def test_delete_first_contact(app):
    app.session.loqin(username="admin", password="secret")
    app.contact.delete_first_contact()
    app.session.logout()
