class ContactList(list):
    def search(self,name):
        matched_contact = []
        for contact in self:
            if name in contact.name:
                matched_contact.append(name)
        return matched_contact


class Contact():
    all_contacts = ContactList()


    def __init__(self,name,email):
        self.name = name
        self.email = email
        Contact.all_contacts.append(self)

class Supplier(Contact):
    def order(self,order):
        print "if this were a real system we should send{} order to {}".format(order,self.name)


class My_Contact(Contact):
    def __init__(self,name,email,phone):
        super.__init__(name,email)
        self.phone = phone