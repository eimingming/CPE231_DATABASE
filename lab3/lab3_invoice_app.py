from helper_functions import *
from Invoice import *
from Product import *
from Customer import *
from PaymentMethod import *
from Receipt import *
from API import *


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
        print("")
        print("*"*50,"create invoice","*"*50)
        create_invoice(invoices, invoiceNo="INT100/20", invoiceDate="2020-01-02", customerCode="Sam", dueDate=None, invoiceLineTuplesList=[{"Product Code":"HD01","Quantity":2,"Unit Price":3000},{"Product Code":"HD02","Quantity":1,"Unit Price":2000}])
        create_invoice(invoices, "INT101/20", "2020-01-04", "CP", None, [{"Product Code":"HD02","Quantity":1,"Unit Price":2000}])
        report_list_all_invoices(invoices, customers, products)
        waitKeyPress("Above are results for creating 2 invoices and line item.")
        
        print("")
        read_invoice(invoices, "INT100/20")
        
        print("")
        print("*"*50,"update invoice","*"*50)      
        update_invoice(invoices, invoiceNo="INT100/20", newInvoiceDate="2020-01-03", newCustomerCode="Sam", newDueDate=None, newInvoiceLineTuplesList=[{"Product Code":"HD01","Quantity":2,"Unit Price":3000},{"Product Code":"HD02","Quantity":1,"Unit Price":2000}])
        #delete_invoice(invoices, "INT101/20")
        report_list_all_invoices(invoices, customers, products)
        waitKeyPress("Results after read, update and delete Invoice")


        print("")
        print("*"*50,"update invoice line","*"*50)
        update_invoice_line(invoices, "INT100/20", "HD02", 8, 1000)
        report_list_all_invoices(invoices, customers, products)
        waitKeyPress("Results after update Invoice Line Item")
        print("")

        #delete_invoice_line(invoices, "INT101/20", "HD02")
        report_list_all_invoices(invoices, customers, products)
        waitKeyPress("Results after delete Invoice Line Item")
        
        #print ("\nTest Report")
        report_products_sold(invoices, products, '2020-01-01', '2020-01-31')
        report_customer_products_sold_list(invoices, products, customers, '2020-01-01', '2020-01-31')
        report_customer_products_sold_total(invoices, products, customers, '2020-01-01', '2020-01-31') 


        #Payment Method 
        print("")
        print("*"*50,"create Payment Method","*"*50)
        PaymentMethods = PaymentMethod()
        create_PaymentMethod(PaymentMethods, "CC", "Credit Card")
        create_PaymentMethod(PaymentMethods, "DC", "Debit Card")
        create_PaymentMethod(PaymentMethods, "PP", "Prompt Pay")
        print("")

        report_list_payment_methods(PaymentMethods)
        waitKeyPress("Above are results for creating.")
        
        print("")
        print("*"*50,"Read Payment Method","*"*50)
        read_PaymentMethod(PaymentMethods, "CC")
        read_PaymentMethod(PaymentMethods, "DD") #error
        #correct the spelling error of "Intle":
       
        print("")
        print("*"*50,"update Payment Method","*"*50)
        update_PaymentMethod(PaymentMethods, "CC", "Credit")
        update_PaymentMethod(PaymentMethods, "DC", "Debit")
        report_list_payment_methods(PaymentMethods)
        waitKeyPress("Results after 2 reads, 2 updates to correct Intle spelling.")

        print("")
        print("*"*50,"delete Payment Method","*"*50)
        delete_PaymentMethod(PaymentMethods, "DD") #error
        delete_PaymentMethod(PaymentMethods, "CC")
        report_list_payment_methods(PaymentMethods)
        waitKeyPress("Results after deleting TT (not exist error).")


        #Create receipt
        receipts = Receipt()
        print("")
        print("*"*50,"create receipt","*"*50)
        create_receipt(receipts,"RCT1001/20","2020-02-04","CP","Cash","Nothing","Paid all invoices partially",[{"Invoice No":"INT100/20","Amount Paid Here":100},{"Invoice No":"INT101/20","Amount Paid Here":200}])
        create_receipt(receipts,"RCT1002/20","2020-02-05","Sam","Credit Card","Master Card, Citibank","Partially paid on INT101/20",[{"Invoice No":"INT100/20","Amount Paid Here":100},{"Invoice No":"INT101/20","Amount Paid Here":200}])
        create_receipt(receipts,"RCT1003/20","2020-02-06","CP","Debit Card","Debit Card","This will later be deleted",[{"Invoice No":"INT100/20","Amount Paid Here":10},{"Invoice No":"INT101/20","Amount Paid Here":20}])
        report_list_all_receipts(receipts,invoices,customers)
        waitKeyPress("Above are results for creating receipt.")
        
        #Read receipt
        read_receipt(receipts, "RCT1001/20")
        read_receipt(receipts, "RCT1003/20")
        read_receipt(receipts, "RCT1005/20")
        report_list_all_receipts(receipts,invoices,customers)
        waitKeyPress("Results of updating 2 receipts: RCT1002/20 (successfully) and RCT1004/20 (unsuccessfully)")

        #Update receipt
        print("")
        print("*"*50,"update receipt","*"*50)
        update_receipt(receipts,"RCT1002/20","2020-02-06","Sam","Credit Card","Master Card, Citibank","Partially paid on INT101/20",[{'Invoice No':'INT100/20','Amount Paid Here':8000},{'Invoice No':'INT101/20','Amount Paid Here':1400}])
        update_receipt(receipts,"RCT1004/20","1999-12-31","Sam","Credit Card","Master Card, Citibank","Partially paid on INT101/20",[{"Invoice No":"INT100/20","Amount Paid Here":8560},{"Invoice No":"INT101/20","Amount Paid Here":1440}])
        report_list_all_receipts(receipts, invoices, customers)
        waitKeyPress("Results after read, update and delete Receipt")
        
        #Delete receipt
        print("")
        print("*"*50,"delete receipt","*"*50)
        delete_receipt(receipts, "RCT1003/20")
        report_list_all_receipts(receipts, invoices, customers)
        waitKeyPress("Results of deleting 2 receipts: RCT1003/20 (successfully) and RCT1005/20 (unsuccessfully)")  

        #Report unpaid invoice 1
        report_unpaid_invoices(invoices,customers,receipts)
        waitKeyPress("Report unpaid invoice 1")

        #Update receipt line
        print("*"*50,"Update receipt line","*"*50)
        print(" ")
        update_receipt_line(receipts,"RCT1001/20","INT100/20", 200)
        update_receipt_line(receipts,"RCT1005/20","INT100/20", 2000)
        update_receipt_line(receipts,"RCT1001/20","INT103/20", 5000)
        report_list_all_receipts(receipts, invoices, customers)
        waitKeyPress("Result of updating 3 receipt line, first successfully, others unsuccessfully")

        #Delete receipt line
        print("*"*50,"Delete receipt line","*"*50)
        print(" ")
        delete_receipt_line(receipts,"RCT1001/20","INT101/20")
        delete_receipt_line(receipts,'RCT1003/20','INT100/20')
        delete_receipt_line(receipts,'RCT1001/20','INT103/20')
        report_list_all_receipts(receipts, invoices, customers)
        waitKeyPress("Result of deleting 3 receipt line, first successfully, others unsuccessfully")
       
        print(" ")
        report_unpaid_invoices(invoices,customers,receipts)

      
    except: #this traps for unexpected system errors
        print ("Unexpected error:", sys.exc_info()[0])
        raise # this line can be erased. It is here to raise another error so you can see which line to debug.
    else:
        print("Normal Termination.   Goodbye!")
#main function ends
#this is so that when called externally via a command line, main is executed.


if __name__ == "__main__":
    main()