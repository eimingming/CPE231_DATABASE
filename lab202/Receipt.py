from helper_functions import *
from Product import *
from Customer import *

class Receipt:
    def __init__(self):
        self.dict = {}
    
    def __updateLineItem (self, receiptLineItemList):
        receiptItemList = []
        total = 0
        for lineItem in receiptLineItemList:
            receiptLineItemDict = {}
            receiptLineItemDict["Invoice No"] = lineItem["Invoice No"]
            receiptLineItemDict["Amount Paid Here"] = lineItem["Amount Paid Here"]
            total += lineItem["Amount Paid Here"]
            receiptItemList.append(receiptLineItemDict)
        return receiptItemList, total

    def create(self, receiptNo, receiptDate, customerCode, paymentMethod, paymentReference, remark, receiptLineItemList):
        if receiptNo in self.dict:
            return {'Is Error': True, 'Error Message': "Receipt No '{}' already exists. Cannot Create. ".format(receiptNo)}
        else:
            receiptLineItemList,total = self.__updateLineItem(receiptLineItemList)
            
            self.dict[receiptNo] = {"Receipt Date" : receiptDate,"Customer Code" : customerCode,"Payment Method" : paymentMethod, "Payment Reference" : paymentReference, "Total Received" : total, "Remarks" : remark,"Items List" : receiptLineItemList}
        return {'Is Error': False, 'Error Message': ""}

    def read(self, receiptNo):
        if receiptNo in self.dict:
            retreceipt = self.dict[receiptNo]
        else:
            return ({'Is Error': True, 'Error Message': "Receipt No '{}' not found. Cannot Read.".format(receiptNo)},{})

        return ({'Is Error': False, 'Error Message': ""},retreceipt)
        
    def update(self, receiptNo, newReceiptDate, newCustomerCode, newPaymentMethod, newPaymentReference, newRemark, newReceiptLineItemList):
        if receiptNo in self.dict:
            self.dict[receiptNo]["Receipt Date"] = newReceiptDate
            self.dict[receiptNo]["Customer Code"] = newCustomerCode
            self.dict[receiptNo]["Payment Method"] = newPaymentMethod
            self.dict[receiptNo]["Payment Reference"] = newPaymentReference
            self.dict[receiptNo]["Remarks"] = newRemark
            receiptLineItemList,total = self.__updateLineItem(newReceiptLineItemList)

            self.dict[receiptNo]["Total Received"] = total
            self.dict[receiptNo]["Items List"] = newReceiptLineItemList
        else:
            return {'Is Error': True, 'Error Message': "Receipt No '{}' not found. Cannot Update.".format(receiptNo)}

        return {'Is Error': False, 'Error Message': ""}

    def delete(self, receiptNo):
        if receiptNo in self.dict:
            del self.dict[receiptNo]
        else:
            return {'Is Error': True, 'Error Message': "Receipt No '{}' not found. Cannot Delete".format(receiptNo)}
        return {'Is Error': False, 'Error Message': ""}

    def dump(self):
        # Will dump all products data by returning 1 dictionary as output.
        return (self.dict)

    def update_receipt_line(self, receiptNo, invoiceNo, amountPaid):
        if receiptNo in self.dict:
            receiptLineItemList = []
            bUpdated = False
            for lineItem in self.dict[receiptNo]["Items List"]:
                invoiceLineItem = {}
                if lineItem["Invoice No"] == invoiceNo:
                    invoiceLineItem["Invoice No"] = invoiceNo
                    invoiceLineItem["Amount Paid Here"] = amountPaid

                    receiptLineItemList.append(invoiceLineItem)
                    bUpdated = True
                else:
                   receiptLineItemList.append(lineItem)
            print(receiptLineItemList)
            
            if bUpdated:
                receiptLineItemList,total = self.__updateLineItem(receiptLineItemList)
                self.dict[receiptNo]["Items List"] = receiptLineItemList
                self.dict[receiptNo]["Total Received"] = total
            else:
                return {'Is Error': True, 'Error Message': "Receipt Code '{}' not found in Invoice No '{}'. Cannot Update.".format(receiptNo,invoiceNo)}
        else:
            return {'Is Error': True, 'Error Message': "Receipt No '{}' not found. Cannot Update.".format(receiptNo)}

        return {'Is Error': False, 'Error Message': ""}

    def delete_receipt_line(self, receiptNo, invoiceNo):
        # The line item of this invoice number is updated to delete this product code.  
        # Note that all the related data in the invoice must be updated such as Total, VAT, and Amount Due. 
        # Returns dictionary {‘Is Error’: ___, ‘Error Message’: _____}
        if receiptNo in self.dict:
            total = 0
            receiptLineItemList = []
            bDeleted = False
            for lineItem in self.dict[receiptNo]["Items List"]:
                if lineItem["Invoice No"] == invoiceNo:
                    bDeleted = True
                else:
                    receiptLineItemList.append(lineItem)
            
            if bDeleted:
                receiptLineItemList, total= self.__updateLineItem(receiptLineItemList)  
                self.dict[receiptNo]["Items List"] = receiptLineItemList
                self.dict[receiptNo]["Total Received"] = total
                
            else:
                return {'Is Error': True, 'Error Message': "Receipt Code '{}' not found in Invoice No '{}'. Cannot Delete.".format(receiptNo, invoiceNo)}
        else:
            return {'Is Error': True, 'Error Message': "Receipt No '{}' not found. Cannot Delete.".format(receiptNo)}

        return {'Is Error': False, 'Error Message': ""}

