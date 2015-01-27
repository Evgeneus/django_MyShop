# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_auto_20150127_0922'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order_Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('kol_product', models.IntegerField(default=0)),
                ('order', models.ForeignKey(to='article.Order')),
                ('product', models.ForeignKey(to='article.Product')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='image',
            name='fifth_image',
            field=models.ImageField(upload_to=b'', verbose_name=b'\xd0\x98\xd0\xb7\xd0\xbe\xd0\xb1\xd1\x80\xd0\xb0\xd0\xb6\xd0\xb5\xd0\xbd\xd0\xb8\xd0\xb5 5', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='image',
            name='fourth_image',
            field=models.ImageField(upload_to=b'', verbose_name=b'\xd0\x98\xd0\xb7\xd0\xbe\xd0\xb1\xd1\x80\xd0\xb0\xd0\xb6\xd0\xb5\xd0\xbd\xd0\xb8\xd0\xb5 4', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='image',
            name='second_image',
            field=models.ImageField(upload_to=b'', verbose_name=b'\xd0\x98\xd0\xb7\xd0\xbe\xd0\xb1\xd1\x80\xd0\xb0\xd0\xb6\xd0\xb5\xd0\xbd\xd0\xb8\xd0\xb5 2', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='image',
            name='third_image',
            field=models.ImageField(upload_to=b'', verbose_name=b'\xd0\x98\xd0\xb7\xd0\xbe\xd0\xb1\xd1\x80\xd0\xb0\xd0\xb6\xd0\xb5\xd0\xbd\xd0\xb8\xd0\xb5 3', blank=True),
            preserve_default=True,
        ),
    ]
