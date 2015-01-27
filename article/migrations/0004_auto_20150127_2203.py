# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0003_auto_20150127_2156'),
    ]

    operations = [
        migrations.AddField(
            model_name='order_product',
            name='sum_product',
            field=models.FloatField(default=0, verbose_name=b'\xd0\xa1\xd1\x83\xd0\xbc\xd0\xbc\xd0\xb0, \xd1\x83. \xd0\xb5.'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='order_product',
            name='kol_product',
            field=models.IntegerField(default=0, verbose_name=b'\xd0\x9a\xd0\xbe\xd0\xbb\xd0\xb8\xd1\x87\xd0\xb5\xd1\x81\xd1\x82\xd0\xb2\xd0\xbe \xd1\x82\xd0\xbe\xd0\xb2\xd0\xb0\xd1\x80\xd0\xb0'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='order_product',
            name='order',
            field=models.ForeignKey(verbose_name=b'\xd0\x97\xd0\xb0\xd0\xba\xd0\xb0\xd0\xb7\xd1\x87\xd0\xb8\xd0\xba', to='article.Order'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='order_product',
            name='product',
            field=models.ForeignKey(verbose_name=b'\xd0\x9d\xd0\xb0\xd0\xb8\xd0\xbc\xd0\xb5\xd0\xbd\xd0\xbe\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5 \xd1\x82\xd0\xbe\xd0\xb2\xd0\xb0\xd1\x80\xd0\xb0', to='article.Product'),
            preserve_default=True,
        ),
        migrations.AlterModelTable(
            name='order_product',
            table='Order_Product',
        ),
    ]
