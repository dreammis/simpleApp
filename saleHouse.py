

class Property():
    def __init__(self,square_feet='',beds='',baths='',**kwargs):
        super.__init__(**kwargs)
        self.square_feet = square_feet
        self.num_bedrooms = beds
        self.num_baths = baths

    def display(self):
        print "PROPERTY DETAILS"
        print "==================="
        print "square footage:{}".format(self.square_feet)
        print "bedrooms:{}".format(self.num_bedrooms)
        print "bathrooms:{}".format(self.num_baths)
        print()

    def prompt_init(self):
        return dict(square_feet = raw_input("Enter the square feet:"),
                    beds = raw_input("Enter the number of bedrooms:"),
                    baths = raw_input("Enther the number of bathrooms:"))

    prompt_init = staticmethod(prompt_init)


class Apartment(Property):
    valid_laundries = ("coin","ensuite","none")
    valid_balconies = ("yes","no","solarium")

    def __init__(self,balcony='',laundry='',**kwargs):
        super.__init__(**kwargs)
        self.balcony = balcony
        self.laundry = laundry

    def display(self):
        super.display()
        print "APARTMENT DETAILS"
        print "laundry:%s"%self.laundry
        print "has balcony:%s"%self.balcony

    def prompt_init(self):

        parent_init=Property.prompt_init()
        laundry = get_valid_input(""
                                  "What laundry facilities does"
                                  "the property have?",
                                  Apartment.valid_laundries)
        balcony = get_valid_input(""
                                  "Does the property have a balcony?",
                                  Apartment.valid_balconies)
        parent_init.update(
            {
                "laundry":laundry,
                "balcony":balcony
            }
        )
        return parent_init
    prompt_init = staticmethod(prompt_init)

class House(Property):
    valid_garage = ("attached","detached","none")
    valid_fenced = ("yes","no")

    def __init__(self,num_stories='',
                 garage='',fenced='',**kwargs):
        super.__init__(**kwargs)
        self.garage = garage
        self.fenced = fenced
        self.num_stories = num_stories

    def display(self):
        super.display()
        print "HOUSE DETAILS"
        print "# of stories:{}".format(self.num_stories)
        print "garage:{}".format(self.garage)
        print "fenced yard:{}".format(self.fenced)

    def prompt_init(self):
        parent_init = Property.prompt_init()
        fenced = get_valid_input("Is the yard fenced?",House.valid_fenced)
        garage = get_valid_input("Is there a garage?",House.valid_garage)
        num_stories = raw_input("How many stories?")
        parent_init.update({
            "fenced":fenced,
            "garage":garage,
            "num_stories":num_stories
        })
        return parent_init
    prompt_init = staticmethod(prompt_init)




def get_valid_input(input_string,valid_options):
    input_string += "({})".format(",".join(valid_options))
    response = raw_input(input_string)
    while response.lower() not in valid_options:
        response = raw_input(input_string)
    return response