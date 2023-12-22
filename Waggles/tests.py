from django.contrib.auth import get_user_model
from django.test import TestCase

from .models import Waggle

User = get_user_model()

# Create your tests here.
class WaggleTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='testuser1', password='testuser1')

    def test_user_exists(self):
        self.assertEqual(self.user.username, "testuser1")

    def test_created_waggle(self):
        waggle_obj = Waggle.objects.create(waggleText="test waggle", user=self.user)
        self.assertEqual(waggle_obj.id, 1)
        self.assertEqual(waggle_obj.user, self.user)
    """
    TODO: Write more tests
    """