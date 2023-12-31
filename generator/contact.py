import random
import string
from model.contact import Contact
import os.path
import jsonpickle
import getopt
import sys


try:
    opts,args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/contacts.json"

for o,a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a



def random_string(prefix,maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + ""*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Contact(firstname="", lastname="",  address="", telephone_mobile="",email="")] + [
    Contact(firstname=random_string("firstname", 10),
            lastname=random_string("lastname", 15),
            address=random_string("address", 30),
            telephone_mobile=random_string("telephone_mobile", 20),
            email=random_string("email", 20))
for i in range(5)
]


file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)


with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))