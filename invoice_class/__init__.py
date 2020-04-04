"""
Robert Walczak"""

#Write an Invoice class with the following data members, which are identified as required or optional in the constructor.
# invoice_id - required
# customer_id - required
# last_name - required
# first_name - required
# phone_number - required
# address - required
# items_with_price - dictionary, optional


class Invoice:
    def __init__(self, invoice_id, customer_id, last_name, first_name, phone_number, address,
                 items_with_price={}):
    
        self.__invoice_id = invoice_id
        self.__customer_id = customer_id
        self.__last_name = last_name
        self.__first_name = first_name
        self.__phone_number = phone_number
        self.__address = address
        self.items_with_price = items_with_price

    def __str__(self):
        return 'Invoice ID: ' + str(self.__invoice_id) + 'Customer ID: ' + str(self.__customer_id) + 'Name' + \
               self.__first_name + " " + self.__last_name + 'Phone Number: ' + self.__phone_number + 'Address: ' + \
               self.__address + "Price List" + str(self.items_with_price)

    def __repr__(self):
        return 'Invoice ID: ' + str(self.__invoice_id) + 'Customer ID: ' + str(self.__customer_id) + 'Name' + \
               self.__first_name + " " + self.__last_name + 'Phone Number: ' + self.__phone_number + 'Address: ' + \
               self.__address + "Price List" + str(self.items_with_price)

    def add_item(self, new_item):
        self.items_with_price.update(new_item)

    def create_invoice(self):
        prdict = self.items_with_price
        tax = round(sum(prdict.values()) * .06, 2)
        total = sum(prdict.values()) + tax
        for key in prdict:
            print(key + "..... $" + str(pdict[key]))
        print("Tax......... " + "{0:.2f}".format(tax))
        print("Total....... " + "{0:.2f}".format(total))


# Driver code
invoice = Invoice(1, 123, '1313 Disneyland Dr, Anaheim, CA 92802' ,'Mouse', 'Minnie', '555-867-5309')
invoice.add_item({'iPad': 799.99})
invoice.add_item({'Surface': 999.99})
invoice.create_invoice()
