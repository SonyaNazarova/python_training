# -*- coding: utf-8 -*-
import pytest
from model.group import Group
from fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_group2(app):
    app.session.loqin(username="admin", password="secret")
    app.group.create(Group(name="2", header="234", footer="2345"))
    app.session.logout()


def test_add_empty_group2(app):
    app.session.loqin(username="admin", password="secret")
    app.group.create(Group(name="", header="", footer=""))
    app.session.logout()