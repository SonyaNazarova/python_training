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
    app.loqin(username="admin", password="secret")
    app.create_group(Group(name="2", header="234", footer="2345"))
    app.logout()


def test_add_empty_group2(app):
    app.loqin(username="admin", password="secret")
    app.create_group(Group(name="", header="", footer=""))
    app.logout()