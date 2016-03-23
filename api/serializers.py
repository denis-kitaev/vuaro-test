# -*- coding: utf-8 -*-
from rest_framework import serializers

from .models import Offer, CustomerProfile, Application


class CustomerProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerProfile


class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        extra_kwargs = {'status': {'read_only': True}}


class OfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Offer


class ApplicationDetailSerializer(serializers.ModelSerializer):
    customer_profile = CustomerProfileSerializer(read_only=True)
    offer = OfferSerializer(read_only=True)

    class Meta:
        model = Application
        extra_kwargs = {'status': {'read_only': True}}
