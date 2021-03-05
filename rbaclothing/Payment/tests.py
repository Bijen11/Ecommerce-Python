from django.test import TestCase
from django.urls import resolve,reverse
from .views import invoice

# Create your tests here.

class TestUrls(TestCase):

    def test_item_detail_url_is_resolved(self):
        url = reverse(invoice)
        self.assertEqual(resolve(url).func,invoice)





