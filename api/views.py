# -*- coding: utf-8 -*-
from django.db.models import Q

import django_filters
from rest_framework import viewsets, permissions, filters
from rest_framework.response import Response
from rest_framework.decorators import detail_route
from rest_condition import Or

from .models import Application, CustomerProfile
from .serializers import ApplicationSerializer, \
    CustomerProfileSerializer, ApplicationDetailSerializer


def user_is_partner(user):
    return hasattr(user, 'partner')


def user_is_credit_organization(user):
    return hasattr(user, 'credit_organization')


class PartnerCanView(permissions.BasePermission):
    def has_permission(self, request, view):
        return (
            request.method in permissions.SAFE_METHODS and
            user_is_partner(request.user)
        )


class PartnerCanCreate(permissions.BasePermission):
    def has_permission(self, request, view):
        return (
            request.method == 'POST' and
            user_is_partner(request.user)
        )


class CreditOrganizationCanView(permissions.BasePermission):
    def has_permission(self, request, view):
        return (
            request.method in permissions.SAFE_METHODS and
            request.user and
            user_is_credit_organization(request.user)
        )


class SuperUserAllowAll(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_superuser


class CustomerProfileFilter(filters.FilterSet):
    score_min = django_filters.NumberFilter(name='score', lookup_type='gte')
    score_max = django_filters.NumberFilter(name='score', lookup_type='lte')

    class Meta:
        model = CustomerProfile
        fields = [
            'date_created', 'date_updated',
            'full_name', 'birth_date',
            'score_min', 'score_max'
        ]


class ApplicationFilter(filters.FilterSet):
    class Meta:
        model = Application
        fields = [
            'date_created', 'date_updated',
            'status', 'offer'
        ]


customer_profile_permission = Or(Or(PartnerCanView, PartnerCanCreate),
                                 SuperUserAllowAll)
application_permission = Or(Or(CreditOrganizationCanView, PartnerCanCreate),
                            SuperUserAllowAll)


class CustomerProfileViewSet(viewsets.ModelViewSet):
    serializer_class = CustomerProfileSerializer
    queryset = CustomerProfile.objects.all()
    permission_classes = [customer_profile_permission, ]
    filter_class = CustomerProfileFilter
    filter_backends = (filters.OrderingFilter,)
    ordering_fields = '__all__'


class ApplicationViewSet(viewsets.ModelViewSet):
    serializer_class = ApplicationSerializer
    permission_classes = [application_permission, ]
    filter_class = ApplicationFilter
    filter_backends = (filters.OrderingFilter,)
    ordering_fields = '__all__'
    queryset = Application.objects \
        .select_related('offer__credit_organization') \
        .select_related('customer_profile').all()

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return ApplicationDetailSerializer
        return super(ApplicationViewSet, self).get_serializer_class()

    def get_queryset(self):
        queryset = super(ApplicationViewSet, self).get_queryset()
        if user_is_credit_organization(self.request.user):
            organization = self.request.user.credit_organization
            queryset = queryset \
                .filter(offer__credit_organization=organization) \
                .filter(Q(status=Application.STATUS_SENT) |
                        Q(status=Application.STATUS_RECEIVED))
        return queryset

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        if user_is_credit_organization(request.user):
            instance.set_received()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    @detail_route(methods=['post'], permission_classes=[PartnerCanCreate])
    def send(self, request, pk=None):
        instance = self.get_object()
        instance.set_sent()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
