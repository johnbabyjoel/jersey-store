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