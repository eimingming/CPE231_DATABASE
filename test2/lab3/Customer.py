from DBHelper import DBHelper
from helper_functions import *

class Customer:
    def __init__(self):
        self.db = DBHelper()

    def create(self, customerCode, customerName, address, creditLimit, country):
        # Adds the new customer record to customers object (dictionary). 
        # Returns dictionary {"Is Error": ___, "Error Message": _____} 
        # Check customer code in products object

        data, columns = self.db.fetch ("SELECT * FROM customer WHERE customer_code = '{}' ".format(customerCode))
        if len(data) > 0:
            return {'Is Error': True, 'Error Message': "Customer code '{}' already exists. Cannot Create. ".format(customerCode)}
        else:
            self.db.execute ("INSERT INTO customer (customer_code,name,address,credit_limit,country) VALUES ('{}' ,'{}','{}','{}','{}')".format(customerCode, customerName, address, creditLimit, country))
        return {'Is Error': False, 'Error Message': ""}

    def read(self, customerCode):
        # Finds the customer code in customers object and returns 1 record in dictionary form. 
        # To return error message + data a tuple returned:  of ({"Is Error": ___, "Error Message": _____}, {<customer data>}) 
        #  where the first one is error message related, and second one is the data.

        data, columns = self.db.fetch ("SELECT customer_code,name,address,credit_limit,country FROM customer WHERE customer_code = '{}' ".format(customerCode))
        if len(data) > 0:
            retCustomer = row_as_dict(data, columns)
        else:
            return ({'Is Error': True, 'Error Message': "Customer Code '{}' not found. Cannot Read.".format(customerCode)},{})

        return ({'Is Error': False, 'Error Message': ""},retCustomer)

    def update(self, customerCode, newCustomerName, newAddress, newCreditLimit, newCountry):
        # Finds the customer code in customers object and then changes the values to the new ones. 
        # Returns dictionary {"Is Error": ___, "Error Message": _____}.

        data, columns = self.db.fetch ("SELECT * FROM customer WHERE customer_code = '{}' ".format(customerCode))
        if len(data) > 0:
            self.db.execute ("UPDATE customer SET name='{}',address='{}',credit_limit='{}',country='{}' WHERE customer_code='{}' ".format(newCustomerName, newAddress, newCreditLimit, newCountry, customerCode))
        else:
            return {'Is Error': True, 'Error Message': "Customer Code '{}' not found. Cannot Update.".format(customerCode)}

        return {'Is Error': False, 'Error Message': ""}

    def delete(self, customerCode):
        # Finds the customer code in customers object and removes it from the dictionary.
        # Returns dictionary {"Is Error": ___, "Error Message": _____}. 

        data, columns = self.db.fetch ("SELECT * FROM customer WHERE customer_code = '{}' ".format(customerCode))
        if len(data) > 0:
            self.db.execute ("DELETE FROM customer WHERE customer_code='{}' ".format(customerCode))
        else:
            return {'Is Error': True, 'Error Message': "Customer Code '{}' not found. Cannot Delete".format(customerCode)}
        return {'Is Error': False, 'Error Message': ""}

    def dump(self):
        # Will dump all customers data and return 1 dictionary as output.

        data, columns = self.db.fetch ('SELECT customer_code as "Costomer Code",name as "Name", address as "Address", credit_limit as "Credit Limit", country as "Country" FROM customer ')
        return row_as_dict(data, columns)