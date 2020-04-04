"""
Robert Walczak
"""


class Customer:

    def __init__(self, customer_id, last_name, first_name, phone_number, address):
        """
        :param first_name: first name of customer
        :param phone_number: phone number of customer
        :param customer_id: ID - numeric
        :param last_name: last name of customer
        :param address: address of customer
        """

        try:
            self.__customer_id = int(customer_id)
        except ValueError:
            raise AttributeError
        self.__last_name = last_name
        self.__first_name = first_name
        self.__phone_number = phone_number
        self.__address = address

    def set__customer_id(self, customer_id):
        self.__customer_id = customer_id

    def set__last_name(self, last_name):
        self.__last_name = last_name

    def set__first_name(self, first_name):
        self.__first_name = first_name

    def set__phone_number(self, phone_number):
        self.__phone_number = phone_number

    def set__address(self, address):
        self.__address = address

    def display(self):
        return str(self.__customer_id) + '\n' + self.__first_name + " " + self.__last_name + \
                 '\n' + self.__phone_number + \
                 '\n' + self.__address

    def __str__(self):
        return str(self.__customer_id) + '\n' + str(self.__first_name) + " " + str(self.__last_name) + \
                 '\n' + str(self.__phone_number) + \
                 '\n' + str(self.__address)

    def __repr__(self):
        return str(self.__customer_id) + '\n' + str(self.__first_name) + " " + str(self.__last_name) + \
                 '\n' + str(self.__phone_number) + \
                 '\n' + str(self.__address)
