from django.shortcuts import render
from django.http import HttpResponse

from .DBHelper import DBHelper

from report.models import *

def index(request):
    invoice_no = request.GET.get('inv','')
    data_report = dict()
    data_report['invoice'] = list(Invoice.objects.filter(invoice_no=invoice_no).select_related('customer_code').values('invoice_no', 'date', 'customer_code_id', 'customer_code__name','due_date','total','vat','amount_due'))
    data_report['invoice_line_item'] = list(InvoiceLineItem.objects.filter(invoice_no=invoice_no).values())
    #return JsonResponse(data_report)
    return render(request, 'report_data.html', data_report)


"""
# Create your views here.
def index(request):
    return render(request, 'index.html')
"""

def ReportListAllInvoices(request):
    db = DBHelper()
    data, columns = db.fetch ('SELECT i.invoice_no as "Invoice No", i.date as "Date" '
                            ' , i.customer_code as "Customer Code", c.name as "Customer Name" '
                            ' , i.due_date as "Due Date", i.total as "Total", i.vat as "VAT", i.amount_due as "Amount Due" '
                            ' , ili.product_code as "Product Code", p.name as "Product Name" '
                            ' , ili.quantity as "Quantity", ili.unit_price as "Unit Price", ili.extended_price as "Extended Price" '
                            ' FROM invoice i JOIN customer c ON i.customer_code = c.customer_code '
                            '  JOIN invoice_line_item ili ON i.invoice_no = ili.invoice_no '
                            '  JOIN product p ON ili.product_code = p.code '
                            ' ')
    data_report = dict()
    data_report['data'] = CursorToDict (data,columns)
    data_report['column_name'] = columns

    return render(request, 'report_list_all_invoices.html', data_report)

def ReportProductsSold(request):
    db = DBHelper()
    data, columns = db.fetch ('SELECT ili.product_code as "Product Code", p.name as "Product Name" '
                              ' , SUM(ili.quantity) as "Total Quantity Sold", SUM(ili.extended_price) as "Total Value Sold" '
                              ' FROM invoice i JOIN invoice_line_item ili ON i.invoice_no = ili.invoice_no '
                              '   JOIN product p ON ili.product_code = p.code '
                              ' GROUP BY p.code, ili.product_code, p.name '
                            ' ')
    data_report = dict()
    data_report['data'] = CursorToDict (data,columns)
    data_report['column_name'] = columns

    return render(request, 'report_products_sold.html', data_report)

def ReportListAllProducts(request):
    db = DBHelper()
    data, columns = db.fetch ('SELECT code as "Code", name as "Name", units as "Units" FROM product '
                              ' ')
    data_report = dict()
    data_report['data'] = CursorToDict (data,columns)
    data_report['column_name'] = columns

    return render(request, 'report_list_all_products.html', data_report)

def CursorToDict(data,columns):
    result = []
    fieldnames = [name.replace(" ", "_").lower() for name in columns]
    for row in data:
        rowset = []
        for field in zip(fieldnames, row):
            rowset.append(field)
        result.append(dict(rowset))
    return result



def ReportListAllReceipt(request):
    db = DBHelper()
    data, columns = db.fetch ('SELECT r.receipt_no as "Receipt No", r.receipt_date as "Receipt Date", r.customer_code as "Customer Code", c.name as "Customer Name" '
                            ', r.payment_method as "Payment Method", r.payment_reference as "Payment Reference", r.remark as "Remark", rli.amount_paid_here As "Total Receipt"'
                            ', i.invoice_no AS "Invoice No", i.Date AS "Invoice Date", i.amount_due AS "Invoice Amount Due" '
                            'FROM receipt r JOIN receipt_line_item rli ON rli.receipt_no = r.receipt_no '
                            'JOIN customer c ON c.customer_code = r.customer_code '
                            'JOIN invoice i ON i.invoice_no = rli.invoice_no Order by r.receipt_no')
    data_report = dict()
    data_report['data'] = CursorToDict (data,columns)
    data_report['column_name'] = columns
    print( data_report['data'])

    return render(request, 'report_list_all_receipt.html', data_report)



def ReportUnpaidInvoices(request):
    db = DBHelper()
    data, columns = db.fetch ('select i.invoice_no AS "Invoice No" , i.date AS "Invoice Date" , c.name AS "Customer Name" , i.amount_due AS "Invoice Amount Due" ,'
                                'sum(rli.amount_paid_here) AS "Invoice Amount Received" , (i.amount_due - sum(rli.amount_paid_here)) As "Invoice Amount Not Paid"'
                                ' FROM receipt r JOIN receipt_line_item rli ON rli.receipt_no = r.receipt_no '
                                'JOIN invoice i ON i.invoice_no = rli.invoice_no '
                                'JOIN customer c ON c.customer_code = i.customer_code '
                                'Group by i.invoice_no, c.name , i.amount_due;')
   
    
    data2, columns2 = db.fetch ('select count("Invoice Amount Not Paid") as "Number of invoices not paid", sum("Invoice Amount Not Paid") as "Total Invoice Amount Not Paid" '
                                'from (SELECT   rli."invoice_no" as "Invoice_No", '
                                ' i.date as "Invoice Date", c.name as "Customer Name" , i."amount_due" as "Amount Received", '
	                            ' SUM(rli.amount_paid_here) as "Amount Paid Here", (i.amount_due - sum(rli.amount_paid_here)) as "Invoice Amount Not Paid" '
	                            ' FROM receipt r JOIN receipt_line_item rli ON r."receipt_no" = rli."receipt_no" '
	                            ' JOIN invoice i ON i."invoice_no" = rli."invoice_no"  '
	                            ' JOIN customer c ON c."customer_code" = i."customer_code" '
	                            ' GROUP BY rli."invoice_no" ,i."date", c."name",i."amount_due") as total_un_re; ')
    data_report = dict()
    data_report['data'] = CursorToDict (data,columns)
    data_report['column_name'] = columns
    data_report['data2'] = CursorToDict (data2,columns2)
    print( data_report['data2'])

    return render(request, 'report_unpaid_invoice.html', data_report)

def ReportListCustomer(request):
    db = DBHelper()
    data, columns = db.fetch ('SELECT c.name AS "Customer Name", line."Total" AS "Total Amount" , SUM(r.total_receipt) AS "Amount Paid", '
                            '(line."Total" - SUM(r.total_receipt)) AS "Amount Not Paid" FROM receipt AS r JOIN (SELECT customer_code, (amount_due) as "Total" '
   		                    'FROM invoice AS i JOIN invoice_line_item AS ilt ON i.invoice_no  = ilt.invoice_no '
  		                    'GROUP BY customer_code, i.amount_due, i.invoice_no) AS line ON r.customer_code = line.customer_code  '
                            'JOIN customer AS c ON c.customer_code = r.customer_code '
                            'GROUP BY c.name, line."Total" ;')
    data_report = dict()
    data_report['data'] = CursorToDict (data,columns)
    data_report['column_name'] = columns
    print( data_report['data'])

    return render(request, 'report_list_customer.html', data_report)
 
  

