from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model

User = get_user_model()

class UserAuthTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.login_url = reverse('login')
        self.logout_url = reverse('logout')
        self.register_url = reverse('register')
        self.books_list_url = reverse('books_list')
        self.check_user_exists_url = reverse('check_user_exists')

        self.user_data = {
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password': 'password123'
        }

        self.user = User.objects.create_user(**self.user_data)

    def test_login_view_get(self):
        response = self.client.get(self.login_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/login.html')

    def test_login_view_post_valid(self):
        response = self.client.post(self.login_url, {
            'username': self.user_data['username'],
            'password': self.user_data['password']
        })
        self.assertRedirects(response, self.books_list_url)

    def test_login_view_post_invalid(self):
        response = self.client.post(self.login_url, {
            'username': self.user_data['username'],
            'password': 'wrongpassword'
        })
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/login.html')
        self.assertContains(response, 'Please enter a correct username and password')

    def test_logout_view(self):
        self.client.login(username=self.user_data['username'], password=self.user_data['password'])
        response = self.client.get(self.logout_url)
        self.assertRedirects(response, self.login_url)

    def test_registration_view_get(self):
        response = self.client.get(self.register_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/register.html')

    def test_registration_view_post_valid(self):
        response = self.client.post(self.register_url, {
            'username': 'newuser',
            'email': 'newuser@example.com',
            'password1': 'newpassword123',
            'password2': 'newpassword123'
        })
        self.assertRedirects(response, self.login_url)
        self.assertTrue(User.objects.filter(username='newuser').exists())

    def test_registration_view_post_invalid(self):
        response = self.client.post(self.register_url, {
            'username': 'newuser',
            'email': 'newuser@example.com',
            'password1': 'newpassword123',
            'password2': 'differentpassword'
        })
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/register.html')

    def test_check_user_exists_view_username(self):
        response = self.client.get(self.check_user_exists_url, {'username': self.user_data['username']})
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(response.content, {'user_check_errors': True, 'email_exists': False, 'username_exists': True})
    def test_check_user_exists_view_email(self):
        response = self.client.get(self.check_user_exists_url, {'email': self.user_data['email']})
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(response.content, {'user_check_errors': True, 'email_exists': True, 'username_exists': False})

    def test_check_user_exists_view_no_data(self):
        response = self.client.get(self.check_user_exists_url)
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(response.content, {'user_check_errors': False, 'email_exists': False, 'username_exists': False})
