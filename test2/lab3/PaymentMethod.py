from DBHelper import DBHelper
from helper_functions import *

class PaymentMethod:
    def __init__(self):
        self.db = DBHelper()


    def create(self, paymentMethodCode, paymentMethodName):

        data, columns = self.db.fetch ("SELECT * FROM payment_method WHERE payment_method_code = '{}' ".format(paymentMethodCode))
        if len(data) > 0:
            return {'Is Error': True, 'Error Message': "Payment Method Code '{}' already exists. Cannot Create. ".format(paymentMethodCode)}
        else:
            self.db.execute ("INSERT INTO payment_method (payment_method_code,payment_method_name) VALUES ('{}' ,'{}')".format(paymentMethodCode, paymentMethodName))
        return {'Is Error': False, 'Error Message': ""}


    def read(self, paymentMethodCode):
        data, columns = self.db.fetch ("SELECT payment_method_code,payment_method_name FROM payment_method WHERE payment_method_code = '{}' ".format(paymentMethodCode))
        if len(data) > 0:
            retPaymentMethod = row_as_dict(data, columns)
        else:
            return ({'Is Error': True, 'Error Message': "Payment Method Code'{}' not found. Cannot Read.".format(paymentMethodCode)},{})

        return ({'Is Error': False, 'Error Message': ""},retPaymentMethod)


    def update(self, paymentMethodCode, newPaymentMethodName):
        data, columns = self.db.fetch ("SELECT * FROM payment_method WHERE payment_method_code = '{}' ".format(paymentMethodCode))
        if len(data) > 0:
            self.db.execute ("UPDATE payment_method SET payment_method_name='{}' WHERE payment_method_code='{}' ".format(newPaymentMethodName, paymentMethodCode))
        else:
            return {'Is Error': True, 'Error Message': "Payment Method Code '{}' not found. Cannot Update.".format(paymentMethodCode)}

        return {'Is Error': False, 'Error Message': ""}


    def delete(self, paymentMethodCode):
        data, columns = self.db.fetch ("SELECT * FROM payment_method WHERE payment_method_code = '{}' ".format(paymentMethodCode))
        if len(data) > 0:
            self.db.execute ("DELETE FROM payment_method WHERE payment_method_code ='{}' ".format(paymentMethodCode))
        else:
            return {'Is Error': True, 'Error Message': "Payment Method Code '{}' not found. Cannot Delete".format(paymentMethodCode)}
        return {'Is Error': False, 'Error Message': ""}


    def dump(self):
        data, columns = self.db.fetch ('SELECT payment_method_code as "Payment Method Code", payment_method_name as "Payment Method Name" FROM payment_method ')
        return row_as_dict(data, columns)