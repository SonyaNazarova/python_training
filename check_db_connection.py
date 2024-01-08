from fixture.orm import ORMFixture
from model.group import Group

db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")

try:
    m = db.get_contacts_in_group(Group(id="232"))
    for item in m:
        print(item)
    print(len(m))
finally:
    pass
