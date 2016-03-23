# -*- coding: utf-8 -*-
from datetime import datetime

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
        co = CreditOrganization.objects.create(user=co_user)

        User.objects.create_superuser(
            'admin', 'admin@test.test', 'adminpasswd')

        offer = Offer.objects.create(**{
            'name': 'Name',
            'date_rotation_begin': datetime.now(),
            'date_rotation_end': datetime.now(),
            'score_min': 1,
            'score_max': 100,
            'credit_organization': co,
            'offer_type': Offer.MORTGAGE
        })

        profile = CustomerProfile.objects.create(**{
            'full_name': 'John Smith',
            'birth_date': '1990-02-12',
            'phone_number': '89031234567',
            'passport_number': '46 96',
            'score': 100
        })

        Application.objects.create(**{
            'customer_profile': profile,
            'offer': offer,
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
            'customer_profile': 1,
            'offer': 1,
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
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.client.logout()

        self.login_co()
        response = self.client.get(self.base_url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
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
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.client.logout()

        self.login_co()
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
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
            'customer_profile': 1,
            'offer': 1,
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

    def test_send(self):
        url = '%s1/send/' % self.base_url
        data = {
            'customer_profile': 1,
            'offer': 1,
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        self.login_partner()
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.client.logout()

        self.login_co()
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.client.logout()

        self.login_admin()
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.client.logout()

    def test_partner_create_send(self):
        self.login_partner()
        profile_data = {
            'full_name': 'John Morris',
            'birth_date': '1990-02-12',
            'phone_number': '89031234567',
            'passport_number': '46 96',
            'score': 103
        }
        resp = self.client.post('/api/customer-profiles/', profile_data, format='json')
        self.assertEqual(resp.status_code, status.HTTP_201_CREATED)

        profile_id = resp.json()['id']
        application_data = {
            'customer_profile': profile_id,
            'offer': 1,
        }

        resp = self.client.post('/api/applications/', application_data, format='json')
        self.assertEqual(resp.status_code, status.HTTP_201_CREATED)

        application_id = resp.json()['id']
        application = Application.objects.get(id=application_id)
        self.assertEqual(application.status, Application.STATUS_NEW)

        self.client.logout()
        self.login_co()
        url = '/api/applications/%s/' % application_id
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, status.HTTP_404_NOT_FOUND)
        self.client.logout()

        self.login_partner()
        url = '/api/applications/%s/send/' % application_id
        resp = self.client.post(url)
        self.assertEqual(resp.status_code, status.HTTP_200_OK)

        application = Application.objects.get(id=application_id)
        self.assertEqual(application.status, Application.STATUS_SENT)

        self.client.logout()

        self.login_co()
        url = '/api/applications/%s/' % application_id
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertEqual(resp.json()['status'], Application.STATUS_RECEIVED)
