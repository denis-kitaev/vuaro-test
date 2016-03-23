# -*- coding: utf-8 -*-
from django.conf.urls import url, include
from . import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'applications', views.ApplicationViewSet)
router.register(r'customer-profiles', views.CustomerProfileViewSet)


urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
