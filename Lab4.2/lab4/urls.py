"""lab4 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from report import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='Index'),
    path('ReportListAllInvoices', views.ReportListAllInvoices),
    path('ReportProductsSold', views.ReportProductsSold),
    path('ReportListAllProducts', views.ReportListAllProducts),
    path('product/list', views.ProductList.as_view(), name='product_list'),
    path('customer/list', views.CustomerList.as_view(), name='customer_list'), 
    path('customer/get/<customer_code>', views.CustomerGet.as_view(), name='customer_get'), 
    path('customer/save', views.CustomerSave.as_view(), name='customer_save'),   
    path('customer/save2', views.CustomerSave2.as_view(), name='customer_save2'), 
    path('paymentMethod/list', views.PaymentMethodList.as_view(), name='paymentMethod_list'),
    path('paymentMethod/save', views.PaymentMethodSave.as_view(), name='paymentMethod_save'),
    path('paymentMethod/save2', views.PaymentMethodSave2.as_view(), name='paymentMethod_save2'),
]
