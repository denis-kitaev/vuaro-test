# -*- coding: utf-8 -*-
from django.db.models import Q

from rest_framework import viewsets, permissions, filters
from rest_framework.response import Response
from rest_framework.decorators import detail_route
from rest_condition import Or

from .models import Application, CustomerProfile
from .serializers import ApplicationSerializer, \
    CustomerProfileSerializer


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
    class Meta:
        model = CustomerProfile
        fields = []


class ApplicationFilter(filters.FilterSet):
    class Meta:
        model = Application
        fields = []


customer_profile_permission = Or(Or(PartnerCanView, PartnerCanCreate),
                                 SuperUserAllowAll)
application_permission = Or(Or(CreditOrganizationCanView, PartnerCanCreate),
                            SuperUserAllowAll)


class CustomerProfileViewSet(viewsets.ModelViewSet):
    serializer_class = CustomerProfileSerializer
    queryset = CustomerProfile.objects.all()
    permission_classes = [customer_profile_permission, ]
    filter_class = CustomerProfileFilter


class ApplicationViewSet(viewsets.ModelViewSet):
    serializer_class = ApplicationSerializer
    queryset = Application.objects \
        .select_related('offer__credit_organization').all()
    permission_classes = [application_permission, ]
    filter_class = ApplicationFilter

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
