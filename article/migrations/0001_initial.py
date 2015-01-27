# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('category', models.CharField(max_length=70, verbose_name=b'\xd0\x9a\xd0\xb0\xd1\x82\xd0\xb5\xd0\xb3\xd0\xbe\xd1\x80\xd0\xb8\xd0\xb8')),
            ],
            options={
                'db_table': 'Category',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=30, verbose_name=b'\xd0\x98\xd0\xbc\xd1\x8f')),
                ('second_name', models.CharField(max_length=30, verbose_name=b'\xd0\xa4\xd0\xb0\xd0\xbc\xd0\xb8\xd0\xbb\xd0\xb8\xd1\x8f')),
                ('phone_number', models.BigIntegerField(default=0, verbose_name=b'\xd0\x9d\xd0\xbe\xd0\xbc\xd0\xb5\xd1\x80 \xd0\xbc\xd0\xbe\xd0\xb1\xd0\xb8\xd0\xbb\xd1\x8c\xd0\xbd\xd0\xbe\xd0\xb3\xd0\xbe')),
                ('email_addres', models.EmailField(max_length=75, verbose_name=b'email-\xd0\xb0\xd0\xb4\xd1\x80\xd0\xb5\xd1\x81')),
                ('city_addres', models.CharField(max_length=30, verbose_name=b'\xd0\x93\xd0\xbe\xd1\x80\xd0\xbe\xd0\xb4')),
            ],
            options={
                'db_table': 'Customer',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('top_image', models.ImageField(upload_to=b'', verbose_name=b'\xd0\x93\xd0\xbb\xd0\xb0\xd0\xb2\xd0\xbd\xd0\xbe\xd0\xb5 \xd0\xb8\xd0\xb7\xd0\xbe\xd0\xb1\xd1\x80\xd0\xb0\xd0\xb6\xd0\xb5\xd0\xbd\xd0\xb8\xd0\xb5')),
                ('second_image', models.ImageField(upload_to=b'', verbose_name=b'\xd0\x98\xd0\xb7\xd0\xbe\xd0\xb1\xd1\x80\xd0\xb0\xd0\xb6\xd0\xb5\xd0\xbd\xd0\xb8\xd0\xb5 2')),
                ('third_image', models.ImageField(upload_to=b'', verbose_name=b'\xd0\x98\xd0\xb7\xd0\xbe\xd0\xb1\xd1\x80\xd0\xb0\xd0\xb6\xd0\xb5\xd0\xbd\xd0\xb8\xd0\xb5 3')),
                ('fourth_image', models.ImageField(upload_to=b'', verbose_name=b'\xd0\x98\xd0\xb7\xd0\xbe\xd0\xb1\xd1\x80\xd0\xb0\xd0\xb6\xd0\xb5\xd0\xbd\xd0\xb8\xd0\xb5 4')),
                ('fifth_image', models.ImageField(upload_to=b'', verbose_name=b'\xd0\x98\xd0\xb7\xd0\xbe\xd0\xb1\xd1\x80\xd0\xb0\xd0\xb6\xd0\xb5\xd0\xbd\xd0\xb8\xd0\xb5 5')),
            ],
            options={
                'db_table': 'Image',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('order_date', models.DateTimeField(verbose_name=b'\xd0\x94\xd0\xb0\xd1\x82\xd0\xb0 \xd0\xb7\xd0\xb0\xd0\xba\xd0\xb0\xd0\xb7\xd0\xb0')),
                ('orders_sum', models.FloatField(verbose_name=b'\xd0\xa1\xd1\x83\xd0\xbc\xd0\xbc\xd0\xb0 \xd0\xb7\xd0\xb0\xd0\xba\xd0\xb0\xd0\xb7\xd0\xb0')),
                ('order_customer', models.ForeignKey(verbose_name=b'\xd0\x97\xd0\xb0\xd0\xba\xd0\xb0\xd0\xb7\xd1\x87\xd0\xb8\xd0\xba', to='article.Customer')),
            ],
            options={
                'db_table': 'Order',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('product_title', models.CharField(max_length=70, verbose_name=b'\xd0\x9d\xd0\xb0\xd0\xb8\xd0\xbc\xd0\xb5\xd0\xbd\xd0\xbe\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5 \xd0\xbf\xd1\x80\xd0\xbe\xd0\xb4\xd1\x83\xd0\xba\xd1\x82\xd0\xb0')),
                ('description', models.TextField(verbose_name=b'\xd0\x9e\xd0\xbf\xd0\xb8\xd1\x81\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5 \xd0\xbf\xd1\x80\xd0\xbe\xd0\xb4\xd1\x83\xd0\xba\xd1\x82\xd0\xb0')),
                ('price_ye', models.FloatField(verbose_name=b'\xd0\xa6\xd0\xb5\xd0\xbd\xd0\xb0(\xd0\xb2 \xd1\x83. \xd0\xb5.)')),
                ('amount', models.IntegerField(default=0, verbose_name=b'\xd0\x9a\xd0\xbe\xd0\xbb\xd0\xb8\xd1\x87\xd0\xb5\xd1\x81\xd1\x82\xd0\xb2\xd0\xbe \xd0\xbd\xd0\xb0 \xd1\x81\xd0\xba\xd0\xbb\xd0\xb0\xd0\xb6\xd0\xb4\xd0\xb5')),
                ('product_category', models.ForeignKey(verbose_name=b'\xd0\x9a\xd0\xb0\xd1\x82\xd0\xb5\xd0\xb3\xd0\xbe\xd1\x80\xd0\xb8\xd0\xb8', to='article.Category')),
            ],
            options={
                'db_table': 'Product',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='order',
            name='products',
            field=models.ManyToManyField(to='article.Product', verbose_name=b'\xd0\x9f\xd0\xb5\xd1\x80\xd0\xb5\xd1\x87\xd0\xb5\xd0\xbd\xd1\x8c \xd0\xb7\xd0\xb0\xd0\xba\xd0\xb0\xd0\xb7\xd0\xb0'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='image',
            name='product',
            field=models.OneToOneField(to='article.Product'),
            preserve_default=True,
        ),
    ]
