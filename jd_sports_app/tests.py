from django.test import TestCase, Client
from .models import Jersey
from django.core.files.uploadedfile import SimpleUploadedFile

class JerseyModelTest(TestCase):
    def setUp(self):
        self.jersey = Jersey.objects.create(
            name='Test Jersey',
            team='Team A',
            size='M',
            price=59.99,
            stock=10
        )

    def test_create_jersey(self):
        self.assertEqual(Jersey.objects.count(), 1)

    def test_update_jersey(self):
        self.jersey.name = "Updated Jersey"
        self.jersey.save()
        self.assertEqual(Jersey.objects.get(id=self.jersey.id).name, "Updated Jersey")

    def test_delete_jersey(self):
        self.jersey.delete()
        self.assertEqual(Jersey.objects.count(), 0)


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

