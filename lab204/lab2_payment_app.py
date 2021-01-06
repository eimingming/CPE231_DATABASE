from helper_functions import *
from Invoice import *
from Product import *
from Customer import *
from PaymentMethod import *
from API import *
######################################################################

#main function
def main():
#main function begins here
    try:
        
        paymentMethods = PaymentMethod() 

        create_payment_method(paymentMethods, "CC", "Credit Card")
        create_payment_method(paymentMethods, "DC", "Debit Card")
        create_payment_method(paymentMethods, "CC", "Prompt Pay")
        report_list_payment_method(paymentMethods)
        waitKeyPress("Above are results for creating")
        
        read_payment_method(paymentMethods, "CC")
        read_payment_method(paymentMethods, "DD") #error
        #correct the spelling error of "Intle":
        update_payment_method(paymentMethods, newName = "Debit",
                        code = "DC")
        update_payment_method(paymentMethods, "CC", "Credit")
        report_list_payment_method (paymentMethods)
        waitKeyPress("Results after 2 reads, 2 updates to correct Intle spelling.")

        delete_payment_method(paymentMethods, "DD") #error
        delete_payment_method(paymentMethods, "CC")
        report_list_payment_method(paymentMethods)
        waitKeyPress("Results after deleting CC (not exist error) and INT99.")

        # pretty print a dictionary (in helper functions):
        printDictData(paymentMethods.dict)
        waitKeyPress("Above is dictionary printed in better format.")
        
    except: #this traps for unexpected system errors
        print ("Unexpected error:", sys.exc_info()[0])
        raise # this line can be erased. It is here to raise another error so you can see which line to debug.
    else:
        print("Normal Termination.   Goodbye!")
#main function ends

#this is so that when called externally via a command line, main is executed.
if __name__ == "__main__":
    main()