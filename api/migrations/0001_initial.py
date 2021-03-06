# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-21 21:10
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='\u0414\u0430\u0442\u0430 \u0438 \u0432\u0440\u0435\u043c\u044f \u0441\u043e\u0437\u0434\u0430\u043d\u0438\u044f')),
                ('date_updated', models.DateTimeField(auto_now=True, verbose_name='\u0414\u0430\u0442\u0430 \u0438 \u0432\u0440\u0435\u043c\u044f \u0438\u0437\u043c\u0435\u043d\u0435\u043d\u0438\u044f')),
                ('status', models.CharField(choices=[(b'NEW', 'NEW'), (b'SENT', 'SENT'), (b'RECEIVED', 'RECEIVED')], max_length=12, verbose_name='\u0421\u0442\u0430\u0442\u0443\u0441')),
            ],
            options={
                'verbose_name': '\u0417\u0430\u044f\u0432\u043a\u0430 \u0432 \u043a\u0440\u0435\u0434\u0438\u0442\u043d\u0443\u044e \u043e\u0440\u0433\u043f\u043d\u0438\u0437\u0430\u0446\u0438\u044e',
                'verbose_name_plural': '\u0417\u0430\u044f\u0432\u043a\u0438 \u0432 \u043a\u0440\u0435\u0434\u0438\u0442\u043d\u0443\u044e \u043e\u0440\u0433\u0430\u043d\u0438\u0437\u0430\u0446\u0438\u044e',
            },
        ),
        migrations.CreateModel(
            name='CreditOrganization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='\u041f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044c')),
            ],
        ),
        migrations.CreateModel(
            name='CustomerProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='\u0414\u0430\u0442\u0430 \u0438 \u0432\u0440\u0435\u043c\u044f \u0441\u043e\u0437\u0434\u0430\u043d\u0438\u044f')),
                ('date_updated', models.DateTimeField(auto_now=True, verbose_name='\u0414\u0430\u0442\u0430 \u0438 \u0432\u0440\u0435\u043c\u044f \u0438\u0437\u043c\u0435\u043d\u0435\u043d\u0438\u044f')),
                ('full_name', models.CharField(max_length=200, verbose_name='\u0424\u0418\u041e')),
                ('birth_date', models.DateField(verbose_name='\u0414\u0430\u0442\u0430 \u0440\u043e\u0436\u0434\u0435\u043d\u0438\u044f')),
                ('phone_number', models.CharField(max_length=15, verbose_name='\u041d\u043e\u043c\u0435\u0440 \u0442\u0435\u043b\u0435\u0444\u043e\u043d\u0430')),
                ('passport_number', models.CharField(max_length=20, verbose_name='\u041d\u043e\u043c\u0435\u0440 \u043f\u0430\u0441\u043f\u043e\u0440\u0442\u0430')),
                ('score', models.IntegerField(verbose_name='\u0421\u043a\u043e\u0440\u0438\u043d\u0433\u043e\u0432\u044b\u0439 \u0431\u0430\u043b\u043b')),
            ],
            options={
                'verbose_name': '\u0410\u043d\u043a\u0435\u0442\u0430 \u043a\u043b\u0438\u0435\u043d\u0442\u0430',
                'verbose_name_plural': '\u0410\u043d\u043a\u0435\u0442\u044b \u043a\u043b\u0438\u0435\u043d\u0442\u043e\u0432',
            },
        ),
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='\u0414\u0430\u0442\u0430 \u0438 \u0432\u0440\u0435\u043c\u044f \u0441\u043e\u0437\u0434\u0430\u043d\u0438\u044f')),
                ('date_updated', models.DateTimeField(auto_now=True, verbose_name='\u0414\u0430\u0442\u0430 \u0438 \u0432\u0440\u0435\u043c\u044f \u0438\u0437\u043c\u0435\u043d\u0435\u043d\u0438\u044f')),
                ('name', models.CharField(max_length=200, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435')),
                ('date_rotation_begin', models.DateTimeField(verbose_name='\u0414\u0430\u0442\u0430 \u0438 \u0432\u0440\u0435\u043c\u044f \u043d\u0430\u0447\u0430\u043b\u0430 \u0440\u043e\u0442\u0430\u0446\u0438\u0438')),
                ('date_rotation_end', models.DateTimeField(verbose_name='\u0414\u0430\u0442\u0430 \u0438 \u0432\u0440\u0435\u043c\u044f \u043e\u043a\u043e\u043d\u0447\u0430\u043d\u0438\u044f \u0440\u043e\u0442\u0430\u0446\u0438\u0438')),
                ('score_min', models.IntegerField(verbose_name='\u041c\u0438\u043d\u0438\u043c\u0430\u043b\u044c\u043d\u044b\u0439 \u0441\u043a\u043e\u0440\u0438\u043d\u0433\u043e\u0432\u044b\u0439 \u0431\u0430\u043b\u043b')),
                ('score_max', models.IntegerField(verbose_name='\u041c\u0430\u043a\u0441\u0438\u043c\u0430\u043b\u044c\u043d\u044b\u0439 \u0441\u043a\u043e\u0440\u0438\u043d\u0433\u043e\u0432\u044b\u0439 \u0431\u0430\u043b\u043b')),
                ('offer_type', models.CharField(choices=[(b'MORTGAGE', '\u0418\u043f\u043e\u0442\u0435\u043a\u0430'), (b'CONSUMER', '\u041f\u043e\u0442\u0440\u0435\u0431\u0438\u0442\u0435\u043b\u044c\u0441\u043a\u0438\u0439'), (b'CAR', '\u0410\u0432\u0442\u043e\u043a\u0440\u0435\u0434\u0438\u0442'), (b'SMSB', '\u041a\u041c\u0421\u0411')], max_length=12, verbose_name='\u0422\u0438\u043f \u043f\u0440\u0435\u0434\u043b\u043e\u0436\u0435\u043d\u0438\u044f')),
                ('credit_organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.CreditOrganization', verbose_name='\u041a\u0440\u0435\u0434\u0438\u0442\u043d\u0430\u044f \u043e\u0440\u0433\u0430\u043d\u0438\u0437\u0430\u0446\u0438\u044f')),
            ],
            options={
                'verbose_name': '\u041f\u0440\u0435\u0434\u043b\u043e\u0436\u0435\u043d\u0438\u0435',
                'verbose_name_plural': '\u041f\u0440\u0435\u0434\u043b\u043e\u0436\u0435\u043d\u0438\u044f',
            },
        ),
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='\u041f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044c')),
            ],
        ),
        migrations.AddField(
            model_name='application',
            name='customer_profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.CustomerProfile', verbose_name='\u0410\u043d\u043a\u0435\u0442\u0430 \u043a\u043b\u0438\u0435\u043d\u0442\u0430'),
        ),
        migrations.AddField(
            model_name='application',
            name='offer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Offer', verbose_name='\u041f\u0440\u0435\u0434\u043b\u043e\u0436\u0435\u043d\u0438\u0435'),
        ),
    ]
