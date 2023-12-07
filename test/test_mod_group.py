from model.group import Group


def test_modify_first_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="old group"))
    app.group.modify_first_group(Group(name="New group"))


def test_modify_first_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(name="old header"))
    app.group.modify_first_group(Group(header="New header"))
