# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
    app.session.loqin(username="admin", password="secret")
    app.group.create(Group(name="2", header="234", footer="2345"))
    app.session.logout()


def test_add_empty_group(app):
    app.session.loqin(username="admin", password="secret")
    app.group.create(Group(name="", header="", footer=""))
    app.session.logout()
