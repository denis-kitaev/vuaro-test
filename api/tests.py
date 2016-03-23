# -*- coding: utf-8 -*-
from django.contrib.auth.models import User

from rest_framework.test import APITestCase
from rest_framework import status

from api.models import CustomerProfile, Application, \
    Offer, Partner, CreditOrganization


class CustomerRequestAPITest(APITestCase):
    base_url = '/api/customer-profiles/'

    def setUp(self):
        partner_user = User.objects.create_user(
            'partner', password='partnerpasswd')
        Partner.objects.create(user=partner_user)

        co_user = User.objects.create_user(
            'credit-organization', password='copasswd')
        CreditOrganization.objects.create(user=co_user)

        User.objects.create_superuser(
            'admin', 'admin@test.test', 'adminpasswd')

        CustomerProfile.objects.create(**{
            'full_name': 'John Smith',
            'birth_date': '1990-02-12',
            'phone_number': '89031234567',
            'passport_number': '46 96',
            'score': 100
        })

    def login_partner(self):
        self.client.login(
            username='partner', password='partnerpasswd')

    def login_co(self):
        self.client.login(
            username='credit-organization', password='copasswd')

    def login_admin(self):
        self.client.login(username='admin', password='adminpasswd')

    def test_create(self):
        data = {
            'full_name': 'John Smith',
            'birth_date': '1990-02-12',
            'phone_number': '89031234567',
            'passport_number': '46 96',
            'score': 100
        }
        response = self.client.post(self.base_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        self.login_partner()
        response = self.client.post(self.base_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.client.logout()

        self.login_co()
        response = self.client.post(self.base_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.client.logout()

        self.login_admin()
        response = self.client.post(self.base_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.client.logout()

    def test_list(self):
        response = self.client.get(self.base_url, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        self.login_partner()
        response = self.client.get(self.base_url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.client.logout()

        self.login_co()
        response = self.client.get(self.base_url, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.client.logout()

        self.login_admin()
        response = self.client.get(self.base_url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.client.logout()

    def test_retrieve(self):
        url = '%s1/' % self.base_url
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        self.login_partner()
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.client.logout()

        self.login_co()
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.client.logout()

        self.login_admin()
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.client.logout()

    def test_delete(self):
        url = '%s1/' % self.base_url
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        self.login_partner()
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.client.logout()

        self.login_co()
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.client.logout()

        self.login_admin()
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.client.logout()

    def test_update(self):
        url = '%s1/' % self.base_url
        data = {
            'full_name': 'John Smith Jr.',
            'birth_date': '1990-03-12',
            'phone_number': '89031234567',
            'passport_number': '46 96',
            'score': 100
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        self.login_partner()
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.client.logout()

        self.login_co()
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.client.logout()

        self.login_admin()
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.client.logout()


class ApplicationAPITest(APITestCase):
    base_url = '/api/applications/'

    def setUp(self):
        partner_user = User.objects.create_user(
            'partner', password='partnerpasswd')
        Partner.objects.create(user=partner_user)

        co_user = User.objects.create_user(
            'credit-organization', password='copasswd')
        CreditOrganization.objects.create(user=co_user)

        User.objects.create_superuser(
            'admin', 'admin@test.test', 'adminpasswd')

        Application.objects.create(**{
            'full_name': 'John Smith',
            'birth_date': '1990-02-12',
            'phone_number': '89031234567',
            'passport_number': '46 96',
            'score': 100
        })

    def login_partner(self):
        self.client.login(
            username='partner', password='partnerpasswd')

    def login_co(self):
        self.client.login(
            username='credit-organization', password='copasswd')

    def login_admin(self):
        self.client.login(username='admin', password='adminpasswd')

    def test_create(self):
        url = '/api/customer-profiles/'
        data = {
            'full_name': 'John Smith',
            'birth_date': '1990-02-12',
            'phone_number': '89031234567',
            'passport_number': '46 96',
            'score': 100
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        self.login_partner()
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.client.logout()

        self.login_co()
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.client.logout()

        self.login_admin()
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.client.logout()

    def test_list(self):
        url = '/api/customer-profiles/'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        self.login_partner()
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.client.logout()

        self.login_co()
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.client.logout()

        self.login_admin()
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.client.logout()

    def test_retrieve(self):
        url = '/api/customer-profiles/1/'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        self.login_partner()
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.client.logout()

        self.login_co()
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.client.logout()

        self.login_admin()
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.client.logout()

    def test_delete(self):
        url = '/api/customer-profiles/1/'
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        self.login_partner()
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.client.logout()

        self.login_co()
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.client.logout()

        self.login_admin()
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.client.logout()

    def test_update(self):
        url = '/api/customer-profiles/1/'
        data = {
            'full_name': 'John Smith Jr.',
            'birth_date': '1990-03-12',
            'phone_number': '89031234567',
            'passport_number': '46 96',
            'score': 100
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        self.login_partner()
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.client.logout()

        self.login_co()
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.client.logout()

        self.login_admin()
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.client.logout()
