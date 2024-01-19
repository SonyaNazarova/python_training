import mysql.connector
from model.group import Group
from model.contact import Contact

class DbFixture:

    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = mysql.connector.connect(host=host, database=name, user=user, password=password, autocommit=True)



    def get_group_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            for row in cursor:
                (id, name, header, footer) = row
                list.append(Group(id=str(id), name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return list

    def get_contact_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute(
                "select id, firstname, lastname, address, home, mobile, work, phone2, email, email2, email3 from addressbook")
            for row in cursor:
                (id, firstname, lastname, address, telephone_home, telephone_mobile, telephone_work, phone2,email, email2, email3) = row
                list.append(Contact(id=str(id), firstname=firstname, lastname=lastname, address=address,
                                    telephone_home=telephone_home, telephone_mobile=telephone_mobile, telephone_work=telephone_work, phone2=phone2,
                                    email=email, email2=email2, email3=email3))
        finally:
            cursor.close()
        return list



    def get_contacts_in_group(self, group):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute(
                "select addressbook.id, addressbook.firstname, addressbook.lastname, addressbook.address, addressbook.home, addressbook.mobile, addressbook.work, addressbook.phone2, addressbook.email, addressbook.email2, addressbook.email3 from addressbook JOIN address_in_groups ON addressbook.id=address_in_groups.id where address_in_groups.group_id=" + group.id)
            for row in cursor:
                (id, firstname, lastname, address, telephone_home, telephone_mobile, telephone_work, phone2,email, email2, email3) = row
                list.append(Contact(id=str(id), firstname=firstname, lastname=lastname, address=address,
                                    telephone_home=telephone_home, telephone_mobile=telephone_mobile, telephone_work=telephone_work, phone2=phone2,
                                    email=email, email2=email2, email3=email3))
        finally:
            cursor.close()
        return list



    def destroy(self):
        self.connection.close()

    def all_contacts_are_in_all_groups(self):
        group_list = self.get_group_list()
        contact_list = self.get_contact_list()
        res = True
        for group in group_list:
            contact_in_groups = self.get_contacts_in_group(group)
            res = res and (all(contact in contact_in_groups for contact in contact_list))
        return res