from sys import maxsize


class Contact:

    def __init__(self, firstname=None, middlename=None, lastname=None, nickname=None, title=None, company=None, address=None,
                 telephone_home=None, telephone_mobile=None, telephone_work=None, fax=None, email=None, email2=None, email3=None, homepage=None, bday=None, bmonth=None,
                 byear=None, aday=None, amonth=None, ayear=None, address2=None, phone2=None, notes=None, id=None,
                 all_phones_from_home_page=None, all_emails=None):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.title = title
        self.company = company
        self.address = address
        self.telephone_home = telephone_home
        self.telephone_mobile = telephone_mobile
        self.telephone_work = telephone_work
        self.fax = fax
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.homepage = homepage
        self.bday = bday
        self.bmonth = bmonth
        self.byear = byear
        self.aday = aday
        self.amonth = amonth
        self.ayear = ayear
        self.address2 = address2
        self.phone2 = phone2
        self.notes = notes
        self.id = id
        self.all_phones_from_home_page = all_phones_from_home_page
        self.all_emails = all_emails


    def __repr__(self):
        return ("%s:%s,%s,%s,%s,%s" % (self.id, self.firstname, self.lastname, self.address,  self.telephone_mobile, self.email))

    def __eq__(self, other):
        return ((self.id is None or other.id is None or self.id ==other.id) and
                (self.firstname is None or other.firstname is None or self.firstname ==other.firstname) and
                (self.lastname is None or other.lastname is None or self.lastname == other.lastname) and
                (self.address is None or other.address is None or self.address == other.address) and
                (self.telephone_mobile is None or other.telephone_mobile is None or self.telephone_mobile == other.telephone_mobile))


    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize

