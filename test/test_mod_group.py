from model.group import Group
import random


def test_modify_group_name(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    old_groups = db.get_group_list()
    group2 = random.choice(old_groups)
    group = Group(name="New group")
    group.id = group2.id
    app.group.modify_group_by_id(group2.id, group)
    new_groups = db.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups.remove(group2)
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)


#def test_modify_group_header(app):
    #    old_groups = app.group.get_group_list()
    #   if app.group.count() == 0:
    #       app.group.create(Group(name="old header"))
    #   app.group.modify_first_group(Group(header="New header"))
    #  new_groups = app.group.get_group_list()
#   assert len(old_groups) == len(new_groups)


