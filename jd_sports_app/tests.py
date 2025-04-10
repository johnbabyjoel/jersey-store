from django.test import TestCase, Client
from .models import Jersey
from django.core.files.uploadedfile import SimpleUploadedFile



class JerseyIntegrationTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_full_crud_flow(self):
        # Create
        response = self.client.post('/add/', {
            'name': 'Flow Jersey',
            'team': 'Team B',
            'size': 'L',
            'price': 79.99,
            'stock': 5
        })
        self.assertEqual(response.status_code, 302)  # Redirect after add
        self.assertEqual(Jersey.objects.count(), 1)

        # Read
        response = self.client.get('/')
        self.assertContains(response, 'Flow Jersey')

        # Update
        jersey_id = Jersey.objects.first().id
        response = self.client.post(f'/edit/{jersey_id}/', {
            'name': 'Updated Flow Jersey',
            'team': 'Team B',
            'size': 'L',
            'price': 79.99,
            'stock': 5
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Jersey.objects.get(id=jersey_id).name, 'Updated Flow Jersey')

        # Delete
        response = self.client.get(f'/delete/{jersey_id}/')
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Jersey.objects.count(), 0)

