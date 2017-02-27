from django.test import TestCase
from django.test import Client
# Create your tests here.
from django.contrib.auth.models import User
from django.shortcuts import HttpResponseRedirect

from django.urls import reverse
from django.core.exceptions import ObjectDoesNotExist

from .forms import RegistrationForm
from  website import forms


class RegistrationFormTestCase(TestCase):
    def setUp(self):

        self.user = User.objects.create_user(username="test", email="test@test.com", password="test")
        self.client = Client()


    def test_valid_form(self):


        response = self.client.post(reverse('user-registration'),

                                    {
                                        'username':'dmravi90',
                                        'password1':'raviteja',
                                        'password2':'raviteja',
                                        'email':'r@gmail.com',

                                    })

        # user = User.objects.get(username='teja123')
        self.assertEqual(response.status_code,302)


    #for valid data
    def test_login_valid_data(self):
        self.client.login(username = self.user.username, password ='test')

        resp = self.client.get(reverse('logged-in'),{'user_id': self.user.id})

        self.assertEqual(resp.status_code, 200)

    #for invalid data
    def test_login_invalid_data(self):
        self.client.login(username='test23', password='raviteja')
        resp = self.client.get(reverse('logged-in'), {'user_id': self.user.id})

        self.assertEqual(resp.status_code, 302)



    #testcase for  invalid form
    def test_registrationform_valid (self):

        form_data = {
                                        'username':'dmravi90',
                                        'password1':'raviteja',
                                        'password2':'raviteja',
                                        'email':'r@gmail.com',

                    }
        form = RegistrationForm(data=form_data)
        self.assertTrue(form.is_valid())
        response = self.client.post(reverse('user-registration'),
                                    form_data,follow=True)


        messages = [m.message for m in list(response.context['messages'])]
        print messages
        self.assertIn('successfully user created',messages)
        self.assertIn('successfully user created', response.content)

        # self.assertFormError(response,'RegistrationForm','username',"user created successfully")

    #testcase for invalid form
    # def test_invalid_form(self):
    #     form_data = {
    #             'username': 'dmravi90',
    #             'password1': '',
    #             'password2': 'raviteja',
    #             'email': 'r@gmail.com',
    #
    #         }
    #     form = RegistrationForm(data=form_data)
    #     self.assertFalse(form.is_valid())
    #     response = self.client.post(reverse('user-registration'),
    #                                 form_data, follow=True)
    #
    #     print response.context['form'].errors












        # user_instance = User.objects.create(username='ravi123',email='rr@gmail.com',password='raviteja',)
        # data ={
        #     'username':user_instance.username,
        #     'email':user_instance.email,
        #     'password':user_instance.password,
        #     # 'password2':user_instance.password2,
        #
        #
        # }
        # form = forms.RegistrationForm(data=data)
        # print form
        # self.assertTrue(form.is_valid() )