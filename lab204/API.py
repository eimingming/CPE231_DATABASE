from helper_functions import *
#This file will contain all API functions calls exposed to outside world for users to use

# function about Product
def create_payment_method(paymentMethod, code, name):
    result = paymentMethod.create(code, name)#returns error dictionary
    if result['Is Error']: #if error
        print(result['Error Message'])
    else:
        print('Payment Method Success.')
    return result #send result for caller program to use

def read_payment_method(paymentMethod, code):
    result = paymentMethod.read(code) #returns tuple of (error dict, data dict)
    if result[0]['Is Error']: #in case error
        print(result[0]['Error Message'])
    else:
        print(result[1])
    return result #send result for caller program to use

def update_payment_method(paymentMethod, code, newName):
    result = paymentMethod.update(code, newName) #returns error dictionary
    if result['Is Error']: #if error
        print(result['Error Message'])
    else:
        print('Payment Method  Success.')
    return result #send result for caller program to use

def delete_payment_method(paymentMethod, code):
    result = paymentMethod.delete(code)#returns error dictionary
    if result['Is Error']: #if error
        print(result['Error Message'])
    else:
        print('Product Delete Success.')
    return result #send result for caller program to use

def report_list_payment_method(paymentMethod):
    result = paymentMethod.dump()
    #printDictInCSVFormat(result, ('Code',), ('Name', 'Units'))
    print (result)
    return result #send result for caller program to use

# function about Product
def create_product(products, code, name, units):
    result = products.create(code, name, units)#returns error dictionary
    if result['Is Error']: #if error
        print(result['Error Message'])
    else:
        print('Product Create Success.')
    return result #send result for caller program to use

def read_product(products, code):
    result = products.read(code) #returns tuple of (error dict, data dict)
    if result[0]['Is Error']: #in case error
        print(result[0]['Error Message'])
    else:
        print(result[1])
    return result #send result for caller program to use

def update_product(products, code, newName, newUnits):
    result = products.update(code, newName, newUnits) #returns error dictionary
    if result['Is Error']: #if error
        print(result['Error Message'])
    else:
        print('Product Update Success.')
    return result #send result for caller program to use

def delete_product(products, code):
    result = products.delete(code)#returns error dictionary
    if result['Is Error']: #if error
        print(result['Error Message'])
    else:
        print('Product Delete Success.')
    return result #send result for caller program to use

def report_list_products(products):
    result = products.dump()
    #printDictInCSVFormat(result, ('Code',), ('Name', 'Units'))
    print (result)
    return result #send result for caller program to use

# function about Customer 
def create_customer(customers, customerCode, customerName, address, creditLimit, country):
    result = customers.create(customerCode, customerName, address, creditLimit, country)#returns error dictionary
    if result['Is Error']: #if error
        print(result['Error Message'])
    else:
        print('Customer Create Success.')
    return result #send result for caller program to use

def read_customer(customers, customerCode):
    result = customers.read(customerCode) #returns tuple of (error dict, data dict)
    if result[0]['Is Error']: #in case error
        print(result[0]['Error Message'])
    else:
        print(result[1])
    return result #send result for caller program to use

def update_customer(customers, customerCode, newCustomerName, newAddress, newCreditLimit, newCountry):
    result = customers.update(customerCode, newCustomerName, newAddress, newCreditLimit, newCountry) #returns error dictionary
    if result['Is Error']: #if error
        print(result['Error Message'])
    else:
        print('Customer Update Success.')
    return result #send result for caller program to use

def delete_customer(customers, customerCode):
    result = customers.delete(customerCode)#returns error dictionary
    if result['Is Error']: #if error
        print(result['Error Message'])
    else:
        print('Customer Delete Success.')
    return result #send result for caller program to use

def report_list_all_customers(customers):
    result = customers.dump()
    printDictInCSVFormat(result, ('Customer Code',), ('Name', 'Address','Credit Limit', 'Country'))
    return result #send result for caller program to use

# function about Invoice 
def create_invoice(invoices, invoiceNo, invoiceDate, customerCode, dueDate, invoiceLineTuplesList):
    result = invoices.create(invoiceNo, invoiceDate, customerCode, dueDate, invoiceLineTuplesList)#returns error dictionary
    if result['Is Error']: #if error
        print(result['Error Message'])
    else:
        print('Invoice Create Success.')
    return result #send result for caller program to use

def read_invoice(invoices, invoiceNo):
    result = invoices.read(invoiceNo) #returns tuple of (error dict, data dict)
    if result[0]['Is Error']: #in case error
        print(result[0]['Error Message'])
    else:
        print(result[1])
    return result #send result for caller program to use

def update_invoice(invoices, invoiceNo, newInvoiceDate, newCustomerCode, newDueDate, newInvoiceLineTuplesList):
    result = invoices.update(invoiceNo, newInvoiceDate, newCustomerCode, newDueDate, newInvoiceLineTuplesList) #returns error dictionary
    if result['Is Error']: #if error
        print(result['Error Message'])
    else:
        print('Invoice Update Success.')
    return result #send result for caller program to use

def delete_invoice(invoices, invoiceNo):
    result = invoices.delete(invoiceNo)#returns error dictionary
    if result['Is Error']: #if error
        print(result['Error Message'])
    else:
        print('Invoice Delete Success.')
    return result #send result for caller program to use

def update_invoice_line(invoices, invoiceNo, productCode, newQuantity, newUnitPrice):
    result = invoices.update_invoice_line(invoiceNo, productCode, newQuantity, newUnitPrice) #returns error dictionary
    if result['Is Error']: #if error
        print(result['Error Message'])
    else:
        print('Invoice Line Item Update Success.')
    return result #send result for caller program to use

def delete_invoice_line(invoices, invoiceNo, productCode):
    result = invoices.delete_invoice_line(invoiceNo, productCode) #returns error dictionary
    if result['Is Error']: #if error
        print(result['Error Message'])
    else:
        print('Invoice Line Item Delete Success.')
    return result #send result for caller program to use

def report_list_all_invoices(invoices, customers, products):
    # Will dump all invoices data and return 1 dictionary as a result (with header and line item joined).  
    # Please show the customer name and product name also. 
    # A helper function such as def print_tabular_dictionary(tabularDictionary) can then be called to print this in a tabular (table-like) form with column headings and data. 

    allInvoice = invoices.dump()
    # re-format result by add Customer Name in object and Product Name in line item
    result = {}
    for invoiceNo, invoiceDetail in allInvoice.items():
        newValue = {}
        for invoiceColume, invoiceData in invoiceDetail.items():
            if invoiceColume == "Customer Code":
                newValue[invoiceColume] = invoiceData
                customer = customers.read(invoiceDetail["Customer Code"])
                if customer[0]['Is Error']:
                    newValue["Customer Name"] = ""
                else:
                    newValue["Customer Name"] = customer[1]["Name"]
            elif invoiceColume == "Items List":
                newLineItemList = []
                for lineItem in invoiceDetail['Items List']:
                    newLineItem = {}
                    for lineItemColume, lineItemData in lineItem.items():
                        if lineItemColume == "Product Code":
                            newLineItem[lineItemColume] = lineItemData
                            
                            product = products.read(lineItem["Product Code"])
                            if product[0]['Is Error']:
                                newLineItem["Product Name"] = ""
                            else:
                                newLineItem["Product Name"] = product[1]["Name"]
                        else:
                            newLineItem[lineItemColume] = lineItemData
                    newLineItemList.append (newLineItem)
                newValue[invoiceColume] = newLineItemList
            else:
                newValue[invoiceColume] = invoiceData
        result[invoiceNo] = newValue
    #print (result)
    printDictInCSVFormat(result, ('Invoice No',), ('Date', 'Customer Code','Due Date','Total','VAT','Amount Due','Items List'))
    return result #send result for caller program to use

def report_products_sold(invoices, products, dateStart, dateEnd):
    # Will return 2 dictionaries: 
    # 1) a dictionary as list of in products sold in the given date range in tabular format of: Product Code, Product Name, Total Quantity Sold, Total Value Sold. Here, (product code) will be unique. 
    # And 2) a second dictionary of the footer will also be returned containing: t the end also show the sum of Total Value Sold.  
    allInvoice = invoices.dump()
    result = {}
    result2 = {}
    sumTotalValueSold = 0
    for key, value in allInvoice.items():
        if (dateStringInDateRange(value['Date'], dateStart, dateEnd)):
            for lineItem in value['Items List']:
                primaryKey = lineItem['Product Code']
                if primaryKey in result:
                    result[primaryKey]['Total Quantity Sold'] += lineItem['Quantity']
                    result[primaryKey]['Total Value Sold'] += lineItem['Extended Price']
                else:
                    product = products.read(lineItem["Product Code"])
                    if product[0]['Is Error']:
                        productName = ""
                    else:
                        productName = product[1]["Name"]
                    result[primaryKey] = {'Product Code':lineItem['Product Code'], 'Product Name':productName,'Total Quantity Sold':lineItem['Quantity'],'Total Value Sold':lineItem['Extended Price']}
                sumTotalValueSold += lineItem['Extended Price']

    result2['Sum of'] = {'Total Value Sold':sumTotalValueSold}
    printDictInCSVFormat(result, (None), ('Product Code','Product Name', 'Total Quantity Sold', 'Total Value Sold'))
    printDictInCSVFormat(result2, (None), ('Total Value Sold',))
    return result.values(), result2

def report_customer_products_sold_list(invoices, products, customers, dateStart, dateEnd):
    # Will return 2 dictionaries: 
    # 1) a dictionary as list of customers and list the products sold to them in the given date range in this format:  Customer Code, Customer Name, Product Code,  Product Name, Invoice No, Invoice Date, Quantity Sold, Value Sold. Here, (customer code, product code, invoice no) will be unique.  
    # And 2) a second footer dictionary showing:  At the end also show the sum of Quantity Sold and sum of Value Sold.
    allInvoice = invoices.dump()
    result = {}
    result2 = {}
    sumTotalQuantitySold = 0
    sumTotalValueSold = 0
    for key, value in allInvoice.items():
        invoiceNo = key
        if (dateStringInDateRange(value['Date'], dateStart, dateEnd)):
            for lineItem in value['Items List']:
                primaryKey = value['Customer Code'] + lineItem['Product Code'] + invoiceNo
                if primaryKey in result:
                    result[primaryKey]['Quantity Sold'] += lineItem['Quantity']
                    result[primaryKey]['Value Sold'] += lineItem['Extended Price']
                else:
                    product = products.read(lineItem["Product Code"])
                    if product[0]['Is Error']:
                        productName = ""
                    else:
                        productName = product[1]["Name"]

                    customer = customers.read(value['Customer Code'])
                    if customer[0]['Is Error']:
                        customerName = ""
                    else:
                        customerName = customer[1]["Name"]
                    result[primaryKey] = {'Customer Code':value['Customer Code'],'Customer Name':customerName,'Product Code':lineItem['Product Code'], 'Product Name':productName,'Invoice No':invoiceNo,'Invoice Date':value['Date'],'Quantity Sold':lineItem['Quantity'],'Value Sold':lineItem['Extended Price']}
                sumTotalQuantitySold += lineItem['Quantity']
                sumTotalValueSold += lineItem['Extended Price']

    result2['Sum of'] = {'Quantity Sold':sumTotalQuantitySold,'Value Sold':sumTotalValueSold}
    printDictInCSVFormat(result, (None), ('Customer Code','Customer Name', 'Product Code', 'Product Name', 'Invoice No', 'Invoice Date', 'Quantity Sold', 'Value Sold'))
    printDictInCSVFormat(result2, (None), ('Quantity Sold','Value Sold'))
    return result.values(), result2

def report_customer_products_sold_total(invoices, products, customers, dateStart, dateEnd):
    allInvoice = invoices.dump()
    result = {}
    result2 = {}
    sumTotalQuantitySold = 0
    sumTotalValueSold = 0
    for key, value in allInvoice.items():
        invoiceNo = key
        if (dateStringInDateRange(value['Date'], dateStart, dateEnd)):
            for lineItem in value['Items List']:
                primaryKey = value['Customer Code'] + lineItem['Product Code']
                if primaryKey in result:
                    result[primaryKey]['Total Quantity Sold'] += lineItem['Quantity']
                    result[primaryKey]['Total Value Sold'] += lineItem['Extended Price']
                else:
                    product = products.read(lineItem["Product Code"])
                    if product[0]['Is Error']:
                        productName = ""
                    else:
                        productName = product[1]["Name"]

                    customer = customers.read(value['Customer Code'])
                    if customer[0]['Is Error']:
                        customerName = ""
                    else:
                        customerName = customer[1]["Name"]
                    result[primaryKey] = {'Customer Code':value['Customer Code'],'Customer Name':customerName,'Product Code':lineItem['Product Code'], 'Product Name':productName,'Total Quantity Sold':lineItem['Quantity'],'Total Value Sold':lineItem['Extended Price']}
                sumTotalQuantitySold += lineItem['Quantity']
                sumTotalValueSold += lineItem['Extended Price']

    result2['Sum of'] = {'Total Quantity Sold':sumTotalQuantitySold,'Total Value Sold':sumTotalValueSold}
    printDictInCSVFormat(result, (None), ('Customer Code','Customer Name', 'Product Code', 'Product Name', 'Total Quantity Sold', 'Total Value Sold'))
    printDictInCSVFormat(result2, (None), ('Total Quantity Sold','Total Value Sold'))
    return result.values(), result2

def report_unpaid_invoices(invoices, customers, receipts):
    total = 0 
    allreceipt = receipts.dump()
    receiptList= []
    for receiptNo, receiptDetail in allreceipt.items(): # Loop receipt
        for receiptColume in receiptDetail:
            if receiptColume == "Items List":
                for lineItem in receiptDetail['Items List']:
                    invoiceDict = {}
                    invoiceDict['Invoice No'] = lineItem['Invoice No']
                    invoiceDict['Amount Paid Here'] = lineItem['Amount Paid Here']
                    invoice = invoices.read(lineItem['Invoice No'])
                    if invoice[0]['Is Error']:
                        invoiceDict = {}
                    else:
                        customer = customers.read(invoice[1]['Customer Code'])
                        if customer[0]['Is Error']:
                            invoiceDict['Customer Name'] = ''
                        else:
                            invoiceDict['Customer Name'] = customer[1]['Name']
                            invoiceDict['Date'] = invoice[1]['Date']
                            invoiceDict['Amount Due'] = invoice[1]['Amount Due']

                            dif = invoiceDict['Amount Due'] - invoiceDict['Amount Paid Here']
                            total += dif
                            invoiceDict['Invoice Amount Not paid'] = dif

                            receiptList.append(invoiceDict)
    printUnPaid(receiptList)
    print("Total Unpaid invoice = ",total)
    print(" ")
    print("----------------------------------------------")





# function about Receipt 
def create_receipt(receipt, receiptNo, receiptDate, customerCode, paymentMethod, paymentReference, remark, receiptLineItemList):
    result = receipt.create(receiptNo, receiptDate, customerCode, paymentMethod, paymentReference, remark, receiptLineItemList)#returns error dictionary
    if result['Is Error']: #if error
        print(result['Error Message'])
    else:
        print('Receipt Create Success.')
    return result #send result for caller program to use

def read_receipt(receipt, receiptNo):
    result = receipt.read(receiptNo) #returns tuple of (error dict, data dict)
    if result[0]['Is Error']: #in case error
        print(result[0]['Error Message'])
    else:
        print(result[1])
    return result #send result for caller program to use

def update_receipt(receipt, receiptNo, newReceiptDate, newCustomerCode, newPaymentMethod, newPaymentReference, newRemark, newReceiptLineItemList):
    result = receipt.update(receiptNo, newReceiptDate, newCustomerCode, newPaymentMethod, newPaymentReference, newRemark, newReceiptLineItemList) #returns error dictionary
    if result['Is Error']: #if error
        print(result['Error Message'])
    else:
        print('Receipt Update Success.')
    return result #send result for caller program to use

def delete_receipt(receipt, receiptNo):
    result = receipt.delete(receiptNo)#returns error dictionary
    if result['Is Error']: #if error
        print(result['Error Message'])
    else:
        print('Invoice Delete Success.')
    return result #send result for caller program to use

def update_receipt_line(Receipt, receiptNo, invoiceNo, amountPaid):
    result = Receipt.update_receipt_line(receiptNo, invoiceNo, amountPaid) #returns error dictionary
    if result['Is Error']: #if error
        print(result['Error Message'])
    else:
        print('Invoice Line Item Update Success.')
    return result #send result for caller program to use

def delete_receipt_line(receipt, receiptNo, invoiceNo):
    result = receipt.delete_receipt_line(receiptNo, invoiceNo) #returns error dictionary
    if result['Is Error']: #if error
        print(result['Error Message'])
    else:
        print('Receipt Line Item Delete Success.')
    return result #send result for caller program to use

def report_list_all_receipt(receipt, invoices, customers):
    allreceipt = receipt.dump()
    # re-format result by add Customer Name in object and Product Name in line item
    result = {}
    for receiptNo, receiptDetail in allreceipt.items():
        newValue = {}
        for receiptColume, receiptData in receiptDetail.items():
            if receiptColume == "Customer Code":
                newValue[receiptColume] = receiptData
                customer = customers.read(receiptDetail["Customer Code"])
                if customer[0]['Is Error']:
                    newValue["Customer Name"] = ""
                else:
                    newValue["Customer Name"] = customer[1]["Name"]

            elif receiptColume == "Items List":
                newLineItemList = []
                for lineItem in receiptDetail['Items List']:
                    newLineItem = {}
                    for lineItemColume, lineItemData in lineItem.items():
                        if lineItemColume == "Invoice No":
                            invoice = invoices.read(lineItem["Invoice No"]) #join
                            if invoice[0]['Is Error']:
                                invoice[1] = ""
                            else:
                                invoice[1]["Invioce No"] = lineItem["Invoice No"]
                                newLineItem = invoice[1]
                    newLineItemList.append (newLineItem)
                newValue[receiptColume] = newLineItemList
            else:
                newValue[receiptColume] = receiptData
        result[receiptNo] = newValue
    #print(result)
    print(" ")
    printForm(result) 
    return result #send result for caller program to use
