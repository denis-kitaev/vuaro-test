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
