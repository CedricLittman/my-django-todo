from django.test import TestCase
from .forms import ItemForm


# Create your tests here.

class TestDjango(TestCase):

    def test_this_thing_works(self):
        self.assertEqual(1, 1)

    def test_this_thing_works2(self):
        self.assertEqual(1, 3)

    def test_this_thing_works3(self):
        self.assertEqual(1, )

    def test_this_thing_works4(self):
        self.assertEqual(1, 4)




class TestItemForm(TestCase):

    def test_item_form_name_not_empty(self):
        form = ItemForm({'name' : ''})
        self.assertFalse(form.is_valid())
        self.assertFails