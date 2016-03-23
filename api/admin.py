# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import Application, CustomerProfile, Offer, \
    Partner, CreditOrganization


class ApplicationAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'date_created', 'customer_profile',
        'offer', 'status'
    ]
    search_fields = [
        'customer_profile__full_name', 'offer__name']


class CustomerProfileAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'date_created', 'full_name',
        'phone_number', 'passport_number'
    ]
    list_display_links = ['id', 'full_name']
    search_fields = [
        'full_name', 'phone_number']


class OfferAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'date_created', 'name',
        'get_offer_type_display'
    ]
    list_display_links = ['id', 'name']
    search_fields = ['name']


class PartnerAndCreditOrganizationAdmin(admin.ModelAdmin):
    search_fields = [
        'user__username', 'user__email']
    list_display = [
        'get_username', 'get_email']

    def get_username(self, obj):
        return obj.user.username
    get_username.short_description = u'Имя пользователя'
    get_username.admin_order_field = 'user__username'

    def get_email(self, obj):
        return obj.user.email
    get_email.short_description = u'Email'
    get_email.admin_order_field = 'user__email'


admin.site.register(Application, ApplicationAdmin)
admin.site.register(CustomerProfile, CustomerProfileAdmin)
admin.site.register(Offer, OfferAdmin)
admin.site.register(Partner, PartnerAndCreditOrganizationAdmin)
admin.site.register(CreditOrganization, PartnerAndCreditOrganizationAdmin)
