def test_delete_first_group(app):
    app.session.loqin(username="admin", password="secret")
    app.group.delete_first_group()
    app.session.logout()
