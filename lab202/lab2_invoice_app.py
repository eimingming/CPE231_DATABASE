from helper_functions import *
from Invoice import *
from Receipt import *
from Product import *
from Customer import *
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
        
        """ 
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
        printDictData(products.dict)
        waitKeyPress("Above is dictionary printed in better format.")

        # pretty print in column format a dictionary (in helper functions):
        printDictInCSVFormat(products.dict, ('Code',), ('Name', 'Units'))
        waitKeyPress("Above is dictionary printed in csv format for copy/paste to excel.")

        
        #shows in case of untrapped exception:
        result = products.dict["HDD5"]
        waitKeyPress("There will be error and exit before you see this.")
        
        """
        customers = Customer()
        create_customer(customers, "Sam", "Sam Co., Ltd.", "122 Bangkok", 500000, "Thailand")
        create_customer(customers, "CP", "Charoen Pokaphan", "14 Sukhumvit, Bangkok", 2000000, "Thailand")
        report_list_all_customers(customers)
        waitKeyPress("Above are results for creating 2 customers.")
        """
        read_customer(customers, "IT City")#error
        read_customer(customers, "Sam")
        #update_customer(customers, newCustomerName = "CPALL", newAddress = "123 Bangkok", newCreditLimit = 100000, newCountry = "Thailand", customerCode = "CP")
        #delete_customer(customers, "CP1")#not found
        #delete_customer(customers, "CP")
        report_list_all_customers(customers)
        waitKeyPress("Results after 2 reads, and update and delete customer CP")
        """
        
        invoices = Invoice()
        create_invoice(invoices, invoiceNo="IN100/20", invoiceDate="2020-01-02", customerCode="Sam", dueDate=None, invoiceLineTuplesList=[{"Product Code":"HD01","Quantity":2,"Unit Price":3000},{"Product Code":"HD02","Quantity":1,"Unit Price":2000}])
        create_invoice(invoices, "IN101/20", "2020-01-04", "Sam", None, [{"Product Code":"HD02","Quantity":1,"Unit Price":2000}])
        report_list_all_invoices(invoices, customers, products)
        waitKeyPress("Above are results for creating 2 invoices and line item.")
        
        """
        read_invoice(invoices, "IN100/20")

        #print ("\nTest Report")
        report_products_sold(invoices, products, '2020-01-01', '2020-01-31')
        report_customer_products_sold_list(invoices, products, customers, '2020-01-01', '2020-01-31')
        report_customer_products_sold_total(invoices, products, customers, '2020-01-01', '2020-01-31')
        
        """
        
        
 #Create_receipt
        print("*"*50,"Create","*"*50)
        receipt = Receipt()
        create_receipt(receipt,"RCT1002/20", 
                                '2020-02-05', 
                                "Sam", "Credit Card", 
                                "Master Card, Citibank", 
                                 "Partially paid on IN101/20", [{"Invoice No" : 'IN100/20',"Amount Paid Here" : 8560},{"Invoice No" : 'IN101/20',"Amount Paid Here" : 1440}])
        read_receipt(receipt,"RCT1002/20")
        print("")

#update_receipt
        print("*"*50,"Update","*"*50)
        update_receipt(receipt, "RCT1002/20", "2020-02-06",  "Sam", "Credit Card", 
                                "Master Card, Citibank", 
                                 "Partially paid on IN101/20", [{"Invoice No" : 'IN100/20',"Amount Paid Here" : 8560},{"Invoice No" : 'IN101/20',"Amount Paid Here" : 1440}])
        read_receipt(receipt,"RCT1002/20")
        print("")

#update_receipt_line 
        print("*"*50,"update_receipt_line ","*"*50)      
        update_receipt_line(receipt, "RCT1002/20" , "IN100/20" , 8000)
        read_receipt(receipt,"RCT1002/20")
        print("")

#delete_receipt_line
        print("*"*50,"delete_receipt_line ","*"*50) 
        delete_receipt_line(receipt,"RCT1002/20","IN100/20")
        read_receipt(receipt,"RCT1002/20")
        print("")

#delete_receipt
        print("*"*50,"delete_receipt ","*"*50) 
        delete_receipt(receipt,"RCT1002/20")
        report_list_all_receipt(receipt,invoices,customers)
        print("")

#Create_receipt
        print("*"*50,"Create receipt","*"*50)
        receipt = Receipt()
        create_receipt(receipt,"RCT1002/20", 
                                '2020-02-05', 
                                "Sam", "Credit Card", 
                                "Master Card, Citibank", 
                                 "Partially paid on IN101/20", [{"Invoice No" : 'IN100/20',"Amount Paid Here" : 8560},{"Invoice No" : 'IN101/20',"Amount Paid Here" : 1440}])
        read_receipt(receipt,"RCT1002/20")
        print("")
   
#ข้อ 3
        print("*"*50,"3 is report list all receipt","*"*50)
        report_list_all_receipt(receipt, invoices, customers)

        
#ข้อ 4
        print("*"*50,"4 is report unpaid invoices","*"*50)
        report_unpaid_invoices(invoices, customers, receipt)
        print("")

     
     
        waitKeyPress("Above are results for creating 2 invoices and line item.")

    except: #this traps for unexpected system errors
        print ("Unexpected error:", sys.exc_info()[0])
        raise # this line can be erased. It is here to raise another error so you can see which line to debug.
    else:
        print("Normal Termination.   Goodbye!")
#main function ends



#this is so that when called externally via a command line, main is executed.



if __name__ == "__main__":
    main()