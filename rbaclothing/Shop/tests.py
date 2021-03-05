from django.test import TestCase, Client
from django.urls import resolve,reverse
from .views import itemdetail, view_product,index
from .models import Product, OrderItem
# Create your tests here.

class TestUrls(TestCase):

    def test_item_detail_url_is_resolved(self):
        url = reverse(itemdetail)
        self.assertEqual(resolve(url).func,itemdetail)

    def test_view_product_url_is_resolved(self):
        url = reverse('view_product', args=['1'])
        self.assertEqual(resolve(url).func,view_product)


class TestViews(TestCase):
    def test_item_detail_GET(self):
        client = Client()

        response = client.get(reverse('index'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response,'shop/index.html')

