from django.test import TestCase

class NightStoreTestCase(TestCase):
    def test_dummy(self):
        """Dummy test"""
        expected = 1
        obtained = 2 
        self.assertEqual(expected, obtained)