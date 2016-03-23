# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User


class Partner(models.Model):
    user = models.OneToOneField(
        User, verbose_name=u'Пользователь')

    def __unicode__(self):
        return unicode(self.user)

    class Meta:
        verbose_name = u'Партнер'
        verbose_name_plural = u'Партнеры'


class CreditOrganization(models.Model):
    user = models.OneToOneField(
        User, related_name='credit_organization',
        verbose_name=u'Пользователь')

    def __unicode__(self):
        return unicode(self.user)

    class Meta:
        verbose_name = u'Кредитная организация'
        verbose_name_plural = u'Кредитные организации'


class BaseModel(models.Model):
    date_created = models.DateTimeField(
        auto_now_add=True, verbose_name=u'Дата создания')
    date_updated = models.DateTimeField(
        auto_now=True, verbose_name=u'Дата изменения')

    class Meta:
        abstract = True


class Offer(BaseModel):
    name = models.CharField(
        max_length=200, verbose_name=u'Название')
    date_rotation_begin = models.DateTimeField(
        verbose_name=u'Дата и время начала ротации')
    date_rotation_end = models.DateTimeField(
        verbose_name=u'Дата и время окончания ротации')
    score_min = models.IntegerField(
        verbose_name=u'Минимальный скоринговый балл')
    score_max = models.IntegerField(
        verbose_name=u'Максимальный скоринговый балл')
    credit_organization = models.ForeignKey(
        CreditOrganization, verbose_name=u'Кредитная организация')

    MORTGAGE = 'MORTGAGE'
    CONSUMER = 'CONSUMER'
    CAR = 'CAR'
    SMSB = 'SMSB'

    OFFER_TYPE_CHOICES = (
        (MORTGAGE, u'Ипотека'),
        (CONSUMER, u'Потребительский'),
        (CAR, u'Автокредит'),
        (SMSB, u'КМСБ'),
    )
    offer_type = models.CharField(
        max_length=12, choices=OFFER_TYPE_CHOICES,
        verbose_name=u'Тип предложения')

    def __unicode__(self):
        return unicode(self.name)

    class Meta:
        verbose_name = u'Предложение'
        verbose_name_plural = u'Предложения'


class CustomerProfile(BaseModel):
    full_name = models.CharField(
        max_length=200, verbose_name=u'ФИО')
    birth_date = models.DateField(
        verbose_name=u'Дата рождения')
    phone_number = models.CharField(
        max_length=15, verbose_name=u'Номер телефона')
    passport_number = models.CharField(
        max_length=20, verbose_name=u'Номер паспорта')
    score = models.IntegerField(
        verbose_name=u'Скоринговый балл')

    def __unicode__(self):
        return unicode(self.full_name)

    class Meta:
        verbose_name = u'Анкета клиента'
        verbose_name_plural = u'Анкеты клиентов'


class Application(BaseModel):
    customer_profile = models.ForeignKey(
        CustomerProfile, verbose_name=u'Анкета клиента')
    offer = models.ForeignKey(
        Offer, verbose_name=u'Предложение')

    STATUS_NEW = 'NEW'
    STATUS_SENT = 'SENT'
    STATUS_RECEIVED = 'RECEIVED'
    STATUS_CHOICES = (
        (STATUS_NEW, u'NEW'),
        (STATUS_SENT, u'SENT'),
        (STATUS_RECEIVED, u'RECEIVED'),
    )
    status = models.CharField(
        max_length=12, choices=STATUS_CHOICES, db_index=True,
        default=STATUS_NEW, verbose_name=u'Статус')

    def __unicode__(self):
        return u'%s - %s' % (self.customer_profile, self.offer)

    class Meta:
        verbose_name = u'Заявка в кредитную оргпнизацию'
        verbose_name_plural = u'Заявки в кредитную организацию'

    def set_received(self):
        self.status = self.STATUS_RECEIVED
        self.save()

    def set_sent(self):
        self.status = self.STATUS_SENT
        self.save()
