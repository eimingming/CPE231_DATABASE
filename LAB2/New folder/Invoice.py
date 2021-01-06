from helper_functions import *
from Product import *
from Customer import *

class Invoice:
    def __init__(self):
        self.dict = {}
    
    def __updateLineItem (self, invoiceLineTuplesList):
        total = 0
        invoiceLineItemList = []
        for lineItem in invoiceLineTuplesList:
            invoiceLineItem = {}
            invoiceLineItem["Product Code"] = lineItem["Product Code"]
            invoiceLineItem["Quantity"] = lineItem["Quantity"]
            invoiceLineItem["Unit Price"] = lineItem["Unit Price"]
            invoiceLineItem["Extended Price"] = lineItem["Quantity"] * lineItem["Unit Price"]
            total = total + invoiceLineItem["Extended Price"]
            invoiceLineItemList.append(invoiceLineItem)
            
        vat = total * 7 / 100
        amountDue = total + vat
        return invoiceLineItemList, total, vat, amountDue

    def create(self, invoiceNo, invoiceDate, customerCode, dueDate, invoiceLineTuplesList):
        # Adds the new invoice record to invoices object (dictionary).
        # Note that the function will calculate Total, VAT, and Amount Due
        #  from the data in the invoiceLineDictList parameter.  
        # The invoiceLineDictList data will be a list of dictionary,
        #  where each dictionary item of the list is in this example
        #  format: {'Product Code': 'HD01',  'Quantity': 2,  'Unit Price': 3000.00}.  
        # Note that for each line item the Extended Price will be calculated by the function using Quantity * Unit Price. 
        # Returns dictionary {‘Is Error’: ___, ‘Error Message’: _____}.

        if invoiceNo in self.dict:
            return {'Is Error': True, 'Error Message': "Invoice No '{}' already exists. Cannot Create. ".format(invoiceNo)}
        else:
            invoiceLineItemList, total, vat, amountDue = self.__updateLineItem(invoiceLineTuplesList)
            
            self.dict[invoiceNo] = {"Invoice Date" : invoiceDate,"Customer Code" : customerCode,"Due Date" : dueDate, "Total" : total, "VAT" : vat, "Amount Due" : amountDue,"Items List" : invoiceLineItemList}
        return {'Is Error': False, 'Error Message': ""}

    def read(self, invoiceNo):
        # Finds the invoice number in invoices object and returns 1invoice  record in dictionary form. 
        # Returns tuple dictionary, one for error, one for the data. 
        if invoiceNo in self.dict:
            retInvoice = self.dict[invoiceNo]
        else:
            return ({'Is Error': True, 'Error Message': "Invoice No '{}' not found. Cannot Read.".format(invoiceNo)},{})

        return ({'Is Error': False, 'Error Message': ""},retInvoice)

    def update(self, invoiceNo, newInvoiceDate, newCustomerCode, newDueDate, newInvoiceLineTuplesList):
        # Finds the invoice number in invoices object and then changes the values to the new ones. 
        # Returns dictionary {‘Is Error’: ___, ‘Error Message’: _____}.
        if invoiceNo in self.dict:
            self.dict[invoiceNo]["Invoice Date"] = newInvoiceDate
            self.dict[invoiceNo]["Customer Code"] = newCustomerCode
            self.dict[invoiceNo]["Due Date"] = newDueDate

            invoiceLineItemList, total, vat, amountDue = self.__updateLineItem(newInvoiceLineTuplesList)
            
            self.dict[invoiceNo]["Total"] = total
            self.dict[invoiceNo]["VAT"] = vat
            self.dict[invoiceNo]["Amount Due"] = amountDue
            self.dict[invoiceNo]["Items List"] = invoiceLineItemList
        else:
            return {'Is Error': True, 'Error Message': "Invoice No '{}' not found. Cannot Update.".format(invoiceNo)}

        return {'Is Error': False, 'Error Message': ""}

    def delete(self, invoiceNo):
        # Finds the invoice number invoices object and removes it from the dictionary. 
        # Returns dictionary {‘Is Error’: ___, ‘Error Message’: _____}.
        if invoiceNo in self.dict:
            del self.dict[invoiceNo]

        else:
            return {'Is Error': True, 'Error Message': "Invoice No '{}' not found. Cannot Delete".format(invoiceNo)}
        return {'Is Error': False, 'Error Message': ""}

    def dump(self):
        # Will dump all products data by returning 1 dictionary as output.
        return (self.dict)

    def update_invoice_line(self, invoiceNo, productCode, newQuantity, newUnitPrice):
        # The line item of this invoice number is updated for this product code.  
        # Note that the extended price must also be recalculated, 
        #  after which all the related data in the invoice must be updated such as Total, VAT, and Amount Due. 
        # Returns dictionary {‘Is Error’: ___, ‘Error Message’: _____}. 
        if invoiceNo in self.dict:
            total = 0
            newInvoiceLineTuplesList = []
            bUpdated = False
            for lineItem in self.dict[invoiceNo]["Items List"]:
                invoiceLineItem = {}
                if lineItem["Product Code"] == productCode:
                    invoiceLineItem["Product Code"] = productCode
                    invoiceLineItem["Quantity"] = newQuantity
                    invoiceLineItem["Unit Price"] = newUnitPrice

                    newInvoiceLineTuplesList.append(invoiceLineItem)
                    bUpdated = True
                else:
                    newInvoiceLineTuplesList.append(lineItem)
            
            if bUpdated:
                invoiceLineItemList, total, vat, amountDue = self.__updateLineItem(newInvoiceLineTuplesList)

                self.dict[invoiceNo]["Total"] = total
                self.dict[invoiceNo]["VAT"] = vat
                self.dict[invoiceNo]["Amount Due"] = amountDue
                self.dict[invoiceNo]["Items List"] = invoiceLineItemList
            else:
                return {'Is Error': True, 'Error Message': "Product Code '{}' not found in Invoice No '{}'. Cannot Update.".format(productCode, invoiceNo)}
        else:
            return {'Is Error': True, 'Error Message': "Invoice No '{}' not found. Cannot Update.".format(invoiceNo)}

        return {'Is Error': False, 'Error Message': ""}

    def delete_invoice_line(self, invoiceNo, productCode):
        # The line item of this invoice number is updated to delete this product code.  
        # Note that all the related data in the invoice must be updated such as Total, VAT, and Amount Due. 
        # Returns dictionary {‘Is Error’: ___, ‘Error Message’: _____}
        if invoiceNo in self.dict:
            total = 0
            invoiceLineItemList = []
            bDeleted = False
            for lineItem in self.dict[invoiceNo]["Items List"]:
                invoiceLineItem = {}
                if lineItem["Product Code"] == productCode:
                    bDeleted = True
                else:
                    invoiceLineItemList.append(lineItem)
            
            if bDeleted:
                invoiceLineItemList, total, vat, amountDue = self.__updateLineItem(invoiceLineItemList)

                self.dict[invoiceNo]["Total"] = total
                self.dict[invoiceNo]["VAT"] = vat
                self.dict[invoiceNo]["Amount Due"] = amountDue
                self.dict[invoiceNo]["Items List"] = invoiceLineItemList
            else:
                return {'Is Error': True, 'Error Message': "Product Code '{}' not found in Invoice No '{}'. Cannot Delete.".format(productCode, invoiceNo)}
        else:
            return {'Is Error': True, 'Error Message': "Invoice No '{}' not found. Cannot Delete.".format(invoiceNo)}

        return {'Is Error': False, 'Error Message': ""}

