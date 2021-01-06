from helper_functions import *
from Receipt import *
from PaymentMethod import *
from Invoice import *
from Customer import *
from API import *

def main():
#main function begins here
    try:        
    
        #Payment Method 
        print("")
        print("*"*50,"create Payment Method","*"*50)
        PaymentMethods = PaymentMethod()
        create_PaymentMethod(PaymentMethods, "CC", "Credit Card")
        create_PaymentMethod(PaymentMethods, "DC", "Debit Card")
        create_PaymentMethod(PaymentMethods, "PP", "Prompt Pay")
        create_PaymentMethod(PaymentMethods, "TM", "Ture Money")
        report_list_payment_methods(PaymentMethods)
        waitKeyPress("Above are results for creating.")
        
        print("")
        print("*"*50,"Read Payment Method","*"*50)
        read_PaymentMethod(PaymentMethods, "CC")
        read_PaymentMethod(PaymentMethods, "DD") #error

        print("")
        print("*"*50,"update Payment Method","*"*50)
        update_PaymentMethod(PaymentMethods, "CC", "Credit")
        update_PaymentMethod(PaymentMethods, "DC", "Debit")
        report_list_payment_methods(PaymentMethods)
        waitKeyPress("Results after 2 reads, 2 updates to correct Intle spelling.")

        print("")
        print("*"*50,"delete Payment Method","*"*50)
        delete_PaymentMethod(PaymentMethods, "DD") #error
        delete_PaymentMethod(PaymentMethods, "TM")
        report_list_payment_methods(PaymentMethods)
        waitKeyPress("Results after deleting TT (not exist error).")

        
    except: #this traps for unexpected system errors
        print ("Unexpected error:", sys.exc_info()[0])
        raise # this line can be erased. It is here to raise another error so you can see which line to debug.
    else:
        print("Normal Termination.   Goodbye!")
#main function ends

#this is so that when called externally via a command line, main is executed.
if __name__ == "__main__":
    main()

