from unittest2 import TestCase

from datalogy import util


class UtilTestCase(TestCase):

    def test_non_empty(self):
        self.assertTrue(util.non_empty([1, 2, 3]))
        self.assertFalse(util.non_empty(['', None]))

    def test_pad_list(self):
        self.assertEquals(
            [1, 2, 3, None],
            util.pad_list([1, 2, 3], 4)
        )

    def test_pad_list_right_size(self):
        self.assertEquals(
            [1, 2, 3],
            util.pad_list([1, 2, 3], 3)
        )
