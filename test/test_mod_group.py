from model.group import Group


def test_mod_first_group(app):
    app.session.loqin(username="admin", password="secret")
    app.group.mod_first_group(Group(name="5000", header="5000", footer="5000"))
    app.session.logout()