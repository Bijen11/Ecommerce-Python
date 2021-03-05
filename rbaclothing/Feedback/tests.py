from django.test import TestCase
from .models import FeedBack

class ModelTest(TestCase):

    def setUp(self):
        FeedBack.objects.create(Name="Rohit", Email="rohit@gmail.com", Subject="Feedback", Message="Testing Success",img="Brothers.jpg")

    def test_orm(self):
        tut = FeedBack.objects.get(Name="Rohit")
        self.assertEqual(tut.Name,"Rohit")

