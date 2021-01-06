# Generated by Django 2.2.2 on 2019-11-01 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='address',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='country',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='credit_limit',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='amount_due',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='due_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='total',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='vat',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='invoicelineitem',
            name='extended_price',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='invoicelineitem',
            name='quantity',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='invoicelineitem',
            name='unit_price',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='units',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
