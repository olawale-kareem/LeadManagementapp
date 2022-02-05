from django.test import TestCase
from LeadApp.models import Lead
from faker import Faker
fake = Faker()


class SomeModelModelTest(TestCase):
    def setUp(self):
        Lead.objects.create(
            name=fake.name(),
            email=fake.email(),
            message=fake.text(),
        )

    def test_save_model(self):
        saved_models = Lead.objects.count()
        self.assertEqual(saved_models, 1)
