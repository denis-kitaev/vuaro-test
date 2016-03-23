# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import Application, CustomerProfile, Offer, \
    Partner, CreditOrganization


class ApplicationAdmin(admin.ModelAdmin):
    pass


class CustomerProfileAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'date_created', 'full_name',
        'phone_number', 'passport_number'
    ]
    list_display_links = ['id', 'full_name']


class OfferAdmin(admin.ModelAdmin):
    pass


class PartnerAdmin(admin.ModelAdmin):
    pass


class CreditOrganizationAdmin(admin.ModelAdmin):
    pass


admin.site.register(Application, ApplicationAdmin)
admin.site.register(CustomerProfile, CustomerProfileAdmin)
admin.site.register(Offer, OfferAdmin)
admin.site.register(Partner, PartnerAdmin)
admin.site.register(CreditOrganization, CreditOrganizationAdmin)
