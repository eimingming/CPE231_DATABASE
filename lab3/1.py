from helper_functions import *
from Invoice import *
from Product import *
from Customer import *
from PaymentMethod import *
from Receipt import *
from API import *
######################################################################
#List of API function calls:
#def create_product(products, code, name, units):
#def read_product(products, code):
#def update_product(products, code, newName, newUnits):
#def delete_product(products, code):
#def report_list_products(products):

#def create_customer(customers, customerCode, customerName, address, creditLimit, country):
#def read_customer(customers, customerCode):
#def update_customer(customers, customerCode, newCustomerName, newAddress, newCreditLimit, newCountry):
#def delete_customer(customers, customerCode):
#def report_list_all_customers(customers):

#def create_invoice(invoices, invoiceNo, invoiceDate, customerCode, dueDate, invoiceLineTuplesList):
#def read_invoice(invoices, invoiceNo):
#def update_invoice(invoices, invoiceNo, newInvoiceDate, newCustomerCode, newDueDate, newInvoiceLineTuplesList):
#def delete_invoice(invoices, invoiceNo):
#def update_invoice_line(invoices, invoiceNo, productCode, newQuantity, newUnitPrice):
#def delete_invoice_line(invoices, invoiceNo, productCode):
#def report_list_all_invoices(invoices, customers, products):

#def report_products_sold(invoices, products, dateStart, dateEnd):
#def report_customer_products_sold_list(invoices, products, customers, dateStart, dateEnd):
#def report_customer_products_sold_total(invoices, products, customers, dateStart, dateEnd):
#######################################################################


#main function
def main():
#main function begins here
    try:
    
        products = Product() # create object products from class Product. Starts as blank dict.
        #'HD01': {'Name': 'Seagate HDD 80 GB', 'Units': 'PCS'},
        # 'HD02': {'Name': 'IBM HDD 60 GB', 'Units': 'PCS'},
        # 'INT01': {'Name': 'Intel Pentium IV 3.6 GHz', 'Units': 'PCS'}}
        
        create_product(products, "HD01", "Seagate HDD 80 GB", "PCS")
        create_product(products, "HD02", "IBM HDD 60 GB", "PCS")
        create_product(products, "INT01", "Intle Pentium IV 3.6 GHz", "PCS")
        create_product(products, "INT99", "Intle Pentium V 4.2 GHz", "PCS")
        report_list_products(products)
        waitKeyPress("Above are results for creating 4 products.")
        
        read_product(products, "HD01")
        read_product(products, "HD99") #error
        #correct the spelling error of "Intle":
        
        update_product(products, newName = "Intel Pentium IV 3.6 GHz", newUnits = "PCS",
                        code = "INT01")
        update_product(products, "INT99", "Intel Pentium V 4.2 GHz", "PCS")
        report_list_products (products)
        waitKeyPress("Results after 2 reads, 2 updates to correct Intle spelling.")
        
        delete_product(products, "INT33") #error
        delete_product(products, "INT99")
        report_list_products(products)
        waitKeyPress("Results after deleting INT33 (not exist error) and INT99.")
        
        # pretty print a dictionary (in helper functions):
        #printDictData(products.dict)
        #waitKeyPress("Above is dictionary printed in better format.")

        # pretty print in column format a dictionary (in helper functions):
        #printDictInCSVFormat(products.dict, ('Code',), ('Name', 'Units'))
        #waitKeyPress("Above is dictionary printed in csv format for copy/paste to excel.")
        

        
        customers = Customer()
        #create_customer(customers, "Sam", "Sam Co., Ltd.", "122 Bangkok", 500000, "Thailand")
        #create_customer(customers, "CP", "Charoen Pokaphan", "14 Sukhumvit, Bangkok", 2000000, "Thailand")

        report_list_all_customers(customers)
        waitKeyPress("Above are results for creating 2 customers.")
        
        read_customer(customers, "IT City")#error
        read_customer(customers, "Sam")
        update_customer(customers, newCustomerName = "CPALL", newAddress = "123 Bangkok", newCreditLimit = 100000, newCountry = "Thailand", customerCode = "CP")
        #delete_customer(customers, "CP1")#not found
        #delete_customer(customers, "CP")
        #report_list_all_customers(customers)
        #waitKeyPress("Results after 2 reads, and update and delete customer CP")

        invoices = Invoice()
        create_invoice(invoices, invoiceNo="INT100/20", invoiceDate="2020-01-02", customerCode="Sam", dueDate=None, invoiceLineTuplesList=[{"Product Code":"HD01","Quantity":2,"Unit Price":3000},{"Product Code":"HD02","Quantity":1,"Unit Price":2000}])
        create_invoice(invoices, "INT101/20", "2020-01-04", "CP", None, [{"Product Code":"HD02","Quantity":1,"Unit Price":2000}])
        report_list_all_invoices(invoices, customers, products)
        waitKeyPress("Above are results for creating 2 invoices and line item.")
        
        read_invoice(invoices, "INT100/20")
        
        update_invoice(invoices, invoiceNo="INT100/20", newInvoiceDate="2020-01-03", newCustomerCode="Sam", newDueDate=None, newInvoiceLineTuplesList=[{"Product Code":"HD01","Quantity":2,"Unit Price":3000},{"Product Code":"HD02","Quantity":1,"Unit Price":2000}])
        #delete_invoice(invoices, "INT101/20")
        report_list_all_invoices(invoices, customers, products)
        waitKeyPress("Results after read, update and delete Invoice")
        
        update_invoice_line(invoices, "INT100/20", "HD02", 8, 1000)
        report_list_all_invoices(invoices, customers, products)
        waitKeyPress("Results after update Invoice Line Item")

        #delete_invoice_line(invoices, "INT101/20", "HD02")
        report_list_all_invoices(invoices, customers, products)
        waitKeyPress("Results after delete Invoice Line Item")
        
        #print ("\nTest Report")
        report_products_sold(invoices, products, '2020-01-01', '2020-01-31')
        
        report_customer_products_sold_list(invoices, products, customers, '2020-01-01', '2020-01-31')
        
        report_customer_products_sold_total(invoices, products, customers, '2020-01-01', '2020-01-31') 


        #Payment Method 
        PaymentMethods = PaymentMethod()
        create_PaymentMethod(PaymentMethods, "T", "Ture Money")
        
        #report_list_payment_method(PaymentMethods)
        #waitKeyPress("Above are results for creating.")
        
        read_PaymentMethod(PaymentMethods, "cc")
        read_PaymentMethod(PaymentMethods, "A") #error
        #correct the spelling error of "Intle":

        update_PaymentMethod(PaymentMethods, "T", "Credit Card")
        #report_list_payment_method(PaymentMethods)
        #waitKeyPress("Results after 2 reads, 2 updates to correct Intle spelling.")

        delete_PaymentMethod(PaymentMethods, "TT") #error
        delete_PaymentMethod(PaymentMethods, "T")
        #report_list_payment_method(paymentMethods)
        #waitKeyPress("Results after deleting TT (not exist error).")




        receipts = Receipt()
        create_receipt(receipts, receiptNo="RCT1001/20", receiptDate="2020-02-04", customerCode="CP", paymenMethod="Cash", paymenReference="Nothing", remark ="Paid all invoices partially" )
        create_receipt(receipts,"RCT1002/20","2020-02-05","Sam","Credit Card","Master Card, Citibank","Partially paid on INT101/20")
        create_receipt(receipts,'RCT1003/20','2020-02-06','CP','Debit Card','Debit Card','This will later be deleted')
        report_list_all_receipts(receipts, invoices, customers)
        waitKeyPress("Above are results for creating receipt.")
        
        read_invoice(receipts, "RCT1001/20")

        update_receipt(receipts,"RCT1002/20","2020-02-06","Sam","Credit Card","Master Card, Citibank","Partially paid on INT101/20")
        #delete_invoice(invoices, "INT101/20")
        report_list_all_receipts(receipts, invoices, customers)
        waitKeyPress("Results after read, update and delete Invoice")
        """
        update_invoice_line(receipts, "INT100/20", "HD02", 8, 1000)
        report_list_all_invoices(receipts, customers, products)
        waitKeyPress("Results after update Invoice Line Item")

        #delete_invoice_line(receipts, "INT101/20", "HD02")
        report_list_all_invoices(receipts, customers, products)
        waitKeyPress("Results after delete Invoice Line Item")
        """
        
    except: #this traps for unexpected system errors
        print ("Unexpected error:", sys.exc_info()[0])
        raise # this line can be erased. It is here to raise another error so you can see which line to debug.
    else:
        print("Normal Termination.   Goodbye!")
#main function ends

#this is so that when called externally via a command line, main is executed.


if __name__ == "__main__":
    main()