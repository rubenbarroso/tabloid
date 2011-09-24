import unittest
from paginator import Paginator

class PaginatorTestCase(unittest.TestCase):
    """ """

    def test_get_page_0(self):
        """ """
        paginator = Paginator(['a', 'b', 'c', 'd'], 2)
        page = paginator.get_page()
        items = [item for item in page]
        self.assertEqual(items[0], 'a')
        self.assertEqual(items[1], 'b')

    def test_get_page_1(self):
        """ """
        paginator = Paginator(['a', 'b', 'c', 'd'], 2)
        page = paginator.get_page(1)
        items = [item for item in page]
        self.assertEqual(items[0], 'c')
        self.assertEqual(items[1], 'd')

    def test_next_page(self):
        """ """
        paginator = Paginator(['a', 'b', 'c', 'd'], 2)
        self.assertEqual(paginator.next_page(), 1)
        self.assertEqual(paginator.next_page(1), None)
        self.assertEqual(paginator.next_page(2), None)

    def test_previous_page(self):
        """ """
        paginator = Paginator(['a', 'b', 'c', 'd'], 2)
        self.assertEqual(paginator.previous_page(), None)
        self.assertEqual(paginator.previous_page(1), 0)