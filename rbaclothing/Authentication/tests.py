from django.test import TestCase

# Create your tests here.
from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from django.contrib.auth.models import User, auth


class ModelTest(TestCase):

    def setUp(self):
        User.objects.create(username="rohitlama1", password="12345", email="rohit123@gmail.com", first_name="rohit", last_name="lama")

    def test_orm(self):
        tut = User.objects.get(username="rohitlama1")
        self.assertEqual(tut.username,"rohitlama1")