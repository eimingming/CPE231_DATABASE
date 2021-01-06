from DBHelper import DBHelper
from helper_functions import *

class PaymentMethod:
    def __init__(self):
        self.db = DBHelper() #เcall helper function

    def create(self, paymentCode, paymentName):
        data, columns = self.db.fetch ("SELECT * FROM payment_method WHERE payment_method_code = '{}'".format(paymentCode))
        if len(data) > 0:
            return {'Is Error': True, 'Error Message': "Payment Method code '{}' already exists. Cannot Create. ".format(paymentCode)}
        else:
            self.db.execute (" INSERT INTO payment_method (payment_method_code,payment_method_name) VALUES ('{}' ,'{}')".format(paymentCode, paymentName))
        return {'Is Error': False, 'Error Message': ""}

    def read(self, paymentCode):
        data, columns = self.db.fetch ('SELECT payment_method_code,payment_method_name FROM "payment_method" WHERE payment_method_code = "{}" '.format(paymentCode))
        if len(data) > 0:
            retPaymentMethod = row_as_dict(data, columns)
        else:
            return ({'Is Error': True, 'Error Message': "Payment Method code '{}' not found. Cannot Read.".format(paymentCode)},{})

        return ({'Is Error': False, 'Error Message': ""},retPaymentMethod)

    def update(self, paymentCode, paymentName):
        data, columns = self.db.fetch ("SELECT * FROM payment_method WHERE payment_method_code = '{}' ".format(paymentCode))
        if len(data) > 0:
            self.db.execute ("UPDATE payment_method SET payment_method_name='{}' WHERE payment_method_code='{}' ".format(newpaymentName))
        else:
            return {'Is Error': True, 'Error Message': "Payment Method code '{}' not found. Cannot Update.".format(paymentCode)}

        return {'Is Error': False, 'Error Message': ""}

    def delete(self, paymentCode):
        data, columns = self.db.fetch ("SELECT * FROM payment_method WHERE payment_method_code = '{}' ".format(paymentCode))
        if len(data) > 0:
            self.db.execute ("DELETE FROM payment_method WHERE payment_method_code='{}' ".format(paymentCode))
        else:
            return {'Is Error': True, 'Error Message': "Payment Method code '{}' not found. Cannot Delete".format(paymentCode)}
        return {'Is Error': False, 'Error Message': ""}

    def dump(self):

        data, columns = self.db.fetch ('SELECT payment_method_code as "Payment Method code", payment_method_name as "Payment Method Name" FROM payment_method ')
        return row_as_dict(data, columns)