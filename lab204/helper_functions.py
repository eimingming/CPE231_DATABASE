import datetime
import calendar
import csv
import sys


#waitKeyPress is useful for debugging to know where you are.
def waitKeyPress(waitMessage):
    waitForKeyPress = input(waitMessage + " (Press a key to continue).")

#helper function to convert from string to date object. Not used yet.
def dateStringToObject(stringDate):
    if stringDate is None:
        return None
    return datetime.datetime.strptime(stringDate, '%Y-%m-%d')

def dateObjectToString(objectDate):
    if objectDate is None:
        return None
    return objectDate.strftime('%Y-%m-%d')

#The helper function below is used to compare 2 dates that are in string format.
def dateStringCompare(stringDate1, comparisonStr, stringDate2):
    objDate1 = dateStringToObject(stringDate1)
    objDate2 = dateStringToObject(stringDate2)

    switcher = {
        "==": objDate1 == objDate2,
        "<": objDate1 < objDate2,
        "<=": objDate1 <= objDate2,
        ">": objDate1 > objDate2,
        ">=": objDate1 >= objDate2,
        "!=": objDate1 != objDate2
    }
    return switcher[comparisonStr] #the comparisonStr will be looked up in switcher dict to get true/false value

#This helper function is used to check if a string date is between 2 string dates
def dateStringInDateRange(theStringDate, stringDateStart, stringDateEnd):
    return dateStringCompare(theStringDate, ">=", stringDateStart) and dateStringCompare(theStringDate,"<=", stringDateEnd)

#used to pretty print a dictionary
def printDictData(dictData):
    print()
    for keys, values in dictData.items():
        print(keys, ':', values)

#used to print a dictionary in CSV form, so you can cut/paste to view it in Excel as a table
# keyFieldTuples are the field names used in the dictionary's keys (usually just 1 field)
# valueFieldTuples are the field names used in dictionary's values (usually many fields)
#Example Call: printDictInCSVFormat(holidays.dict, ('date',), ('holidayName', 'numberDaysOff'))
def printDictInCSVFormat(dictData, keyFieldTuples, valueFieldTuples ):
    print()
    if keyFieldTuples is not None:
        for i in range(len(keyFieldTuples)):
            if (i==0):
                print(keyFieldTuples[i], end='')
            else:
                print(",", keyFieldTuples[i], end = '')

    for i in range(len(valueFieldTuples)):
        if keyFieldTuples is None and (i == len(valueFieldTuples)-1 and i == 0):
            print(valueFieldTuples[i])
        elif keyFieldTuples is None and i == 0:
            print(valueFieldTuples[i], end='')
        else:
            if (i == len(valueFieldTuples)-1):
                print(",", valueFieldTuples[i])
            else:
                print(",", valueFieldTuples[i], end='')

    for keys, values in dictData.items():
        if keyFieldTuples is not None:
            keyLength = len(keyFieldTuples)
        else:
            keyLength = 0
        if (keyLength == 1):
            print(keys, end='')
        else:
            for i in range(keyLength):
                if (i == 0):
                    print(keys[i], end='')
                else:
                    print(",", keys[i], end='')
        for i in range(len(valueFieldTuples)):
            if keyFieldTuples is None and (i == len(valueFieldTuples) - 1 and i == 0):
                print(values[valueFieldTuples[i]])
            elif keyFieldTuples is None and i == 0:
                print(values[valueFieldTuples[i]], end='')
            elif (i == len(valueFieldTuples) - 1):
                print(",", values[valueFieldTuples[i]])
            else:
                print(",", values[valueFieldTuples[i]], end='')


def printForm(dict):
    for i in dict:
        print("Customer Name :",dict[i]["Customer Name"])
        print("__________________________________________________________________________________________________________________________________________________________")
        print("Invioce No",end = "  ,    ")
        print("Date",end = "    ,  ")
        print("Customer Code",end = "  ,  ")
        print("Due Date",end = "  ,  ")
        print("Total",end = "  ,   ")
        print("VAT",end = "   ,  ")
        print("Amount Due",end = "  ,  ")
        print("Items List")
        print("__________________________________________________________________________________________________________________________________________________________")
        print(" ")
        items = dict[i]["Items List"]
        for j in items:
            print(j ["Invioce No"],end = "  ,  ")
            print(j ["Date"],end = "  ,       ")
            print(j ["Customer Code"],end = "       ,    ")
            print(j ["Due Date"],end = "    ,   ")
            print(j ["Total"],end = "  ,  ")
            print(j ["VAT"],end = "  ,    ")
            print(j ["Amount Due"],end = "    ,  ")
            print(j ["Items List"])
    
    print(" ")
    print(" ")
    print(" ")



def  printUnPaid(dict):
    print("__________________________________________________________________________________________________________________________________________________________")
    print("Invoice Number",end = "   ,  ")
    print("Invoice Date",end = "    ,   ")
    print("Customer Name",end = "   ,   ")
    print("Invoice Amount Due",end = "   ,   ")
    print("Invoice Amount Received",end = "   ,   ")
    print("Invoice Amount Not Paid")
    
    print("__________________________________________________________________________________________________________________________________________________________")
    print(" ")
    for i in dict:
        print(i ["Invoice No"],end = "         ,    ")
        print(i ["Date"],end = "    ,   ")
        print(i ["Customer Name"],end = "   ,         ")
        print(i ["Amount Due"],end = "         ,            ")
        print(i ["Amount Paid Here"],end = "             ,          ")
        print(i ["Invoice Amount Not paid"])
    print("__________________________________________________________________________________________________________________________________________________________")
        


    