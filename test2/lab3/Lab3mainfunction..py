from helper_functions import *
from Receipt import *
from PaymentMethod import *
from Invoice import *
from Customer import *
from API import *

def main():
#main function begins here
    try:
        products = Product()
        create_product(products, "HD01", "Seagate HDD 80 GB", "PCS")
        create_product(products, "HD02", "IBM HDD 60 GB", "PCS")
        create_product(products, "INT01", "Intel Pentium IV 3.6 GHz", "PCS")
        report_list_products(products)
        waitKeyPress("These are 3 products in the database")
        
        customers = Customer()
        create_customer(customers, "Sam", "Sam Co., Ltd.", "122 Bangkok", 500000, "Thailand")
        create_customer(customers, "CP", "CPALL", "123 Bangkok", 100000, "Thailand")
        report_list_all_customers(customers)
        waitKeyPress("These are 2 customers in the database")
               
        invoices = Invoice()
        create_invoice(invoices, invoiceNo="INT100/20", invoiceDate="2020-01-03", customerCode="Sam", dueDate=None, invoiceLineTuplesList=[{"Product Code":"HD01","Quantity":2,"Unit Price":3000},{"Product Code":"HD02","Quantity":8,"Unit Price":1000}])
        create_invoice(invoices, "INT101/20", "2020-01-04", "CP", None, [{"Product Code":"HD02","Quantity":1,"Unit Price":2000}])
        create_invoice(invoices, "INT102/20", "2020-01-04", "CP", None, [{"Product Code":"HD02","Quantity":1,"Unit Price":2500}])
        report_list_all_invoices(invoices, customers, products)
        waitKeyPress("These are 2 invoices in the database")
        delete_invoice(invoices,"INT104/20")    
        delete_invoice(invoices,"INT105/20") 

        receipts = Receipt()
        create_receipt(receipts,'RCT1001/20','2020-02-04','CP','Cash','Nothing','Paid all invoices partially',[{'Invoice No':'INT100/20','Amount Paid Here':100},{'Invoice No':'INT101/20','Amount Paid Here':200}])
        create_receipt(receipts,'RCT1002/20','2020-02-05','Sam','Credit Card','Master Card, Citibank','Partially paid on INT101/20',[{'Invoice No':'INT100/20','Amount Paid Here':8560},{'Invoice No':'INT101/20','Amount Paid Here':1440}])
        create_receipt(receipts,'RCT1003/20','2020-02-06','CP','Debit Card','Debit Card','This will later be deleted',[{'Invoice No':'INT100/20','Amount Paid Here':10},{'Invoice No':'INT102/20','Amount Paid Here':1000}])
        report_list_all_receipts(receipts,invoices,customers)
        waitKeyPress("Results of creating 3 receipts: RCT1001/20, RCT1002/20, and RCT1003/20")
    
        #Read receipt
        read_receipt(receipts,'RCT1003/20')
        read_receipt(receipts,'RCT1005/20')
        report_list_all_receipts(receipts,invoices,customers)
        waitKeyPress("Results of reading 2 receipts: RCT1003/20 (successfully), and RCT1005/20 (unsuccessfully)")
        
        #Update receipt
        update_receipt(receipts,'RCT1002/20','2020-02-06','Sam','Debit Card','VISA card','Partially paid on INT100/20 and INT101/20',[{'Invoice No':'INT100/20','Amount Paid Here':8000},{'Invoice No':'INT101/20','Amount Paid Here':1400}])
        update_receipt(receipts,'RCT1004/20','1999-12-31','Sam','Credit Card','Master Card, Citibank','Partially paid on INT101/20',[{'Invoice No':'INT100/20','Amount Paid Here':8560},{'Invoice No':'INT101/20','Amount Paid Here':1440}])
        report_list_all_receipts(receipts,invoices,customers)
        waitKeyPress("Results of updating 2 receipts: RCT1002/20 (successfully) and RCT1004/20 (unsuccessfully)")
        
        #Delete receipt
        delete_receipt(receipts,'RCT1005/20')
        report_list_all_receipts(receipts,invoices,customers)
        waitKeyPress("Results of deleting 2 receipts: RCT1003/20 (successfully) and RCT1005/20 (unsuccessfully)")

        #Report unpaid invoice 1
        report_unpaid_invoices(invoices,customers,receipts)
        waitKeyPress("Report unpaid invoice 1")

        #Update receipt line
        update_receipt_line(receipts,'RCT1001/20','INT100/20',200)
        update_receipt_line(receipts,'RCT1005/20','INT100/20',2000)
        update_receipt_line(receipts,'RCT1001/20','INT103/20',3000)
        report_list_all_receipts(receipts,invoices,customers)
        waitKeyPress("Result of updating 3 receipt line, first successfully, others unsuccessfully")

        #Delete receipt line
        delete_receipt_line(receipts,'RCT1001/20','INT101/20')
        delete_receipt_line(receipts,'RCT1003/20','INT100/20')
        delete_receipt_line(receipts,'RCT1001/20','INT103/20')
        report_list_all_receipts(receipts,invoices,customers)
        waitKeyPress("Result of deleting 3 receipt line, first successfully, others unsuccessfully")

        #print ("\nTest Report")
        #report_products_sold(invoices, products, '2020-01-01', '2020-01-31')
        #report_customer_products_sold_list(invoices, products, customers, '2020-01-01', '2020-01-31')
        #report_customer_products_sold_total(invoices, products, customers, '2020-01-01', '2020-01-31')
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