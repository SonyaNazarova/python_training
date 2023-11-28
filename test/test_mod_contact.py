from model.contact import Group


def test_mod_first_contact(app):
    app.session.loqin(username="admin", password="secret")
    app.contact.mod_first_contact(Group(firstname="000", middlename="000", lastname="000", nickname="000", title="000", address="000", company="000",
                                        telephone_home="000", telephone_mobile="0000",
                             telephone_work="0000", fax="0000", email="10", email2="100", email3="200", homepage="000", bday="12",
                             bmonth="February", byear="1900", aday="10", amonth="January", ayear="2020", address2="30", phone2="000", notes="000"))
    app.session.logout()