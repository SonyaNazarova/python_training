# -*- coding: utf-8 -*-
import pytest
from contact import Group
from application import Application

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.loqin(username="admin", password="secret")
    app.create_contact(Group(firstname="2", middlename="1", lastname="3", nickname="4", title="5", address="7",
         company="6", telephone_home="8", telephone_mobile="9", telephone_work="10", fax="11", email="12", email2="13", email3="14",
         homepage="15", bday="9",bmonth="January", byear="1988", aday="14", amonth="February", ayear="2000",address2="16", phone2="17", notes="18"))
    app.logout()