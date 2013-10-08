from unittest2 import TestCase

from datalogy import html


class HtmlTestCase(TestCase):

    row = [1, 2, 3]
    labelled_row = ['TRAIN NO.', '0116', '0118', '0120', 'TRAIN NO.', '0124']

    def test_parse_html(self):
        self.assertTrue(
            isinstance(
                html.parse_html_table('<html></html>'),
                list
            )
        )

    def test_pad_list(self):
        self.assertEquals(
            self.row + [None],
            html.pad_list(self.row, 4)
        )

    def test_pad_list_right_size(self):
        self.assertEquals(
            self.row,
            html.pad_list(self.row, 3)
        )

    def test_non_empty(self):
        self.assertTrue(html.non_empty(self.row))
        self.assertFalse(html.non_empty(['', None]))

    def test_normalise_tabular_labelling(self):
        self.assertEquals(
            ['0116', '0118', '0120', '0124'],
            html.normalise_tabular_labelling(self.labelled_row, 'TRAIN NO.')
        )

    def test_clean_table(self):
        self.assertEquals(
            [
                [2, 3],
                [3, 'somestring'],
            ],
            html.clean_table([
                [None],
                [2, 3, '&nbsp;'],
                [None, 3, 'somestring'],
            ])
        )

        self.assertEquals(
            [
                [1], [2], [3],
            ],
            html.clean_table([
                [None, 1],
                [None, 2],
                [None, 3],
            ])
        )

    def test_strip_unprintables(self):
        row = [u'\xa0FISH HOEK', '00:03 ', '04:36 ', '05:36 ', '06:34 ', '07:30 ', '08:29 ', '09:16 ', '09:40 ', '10:07 ', '10:54 ', '12:05 ', u'\xa0FISH HOEK', '13:12 ', '13:53 ', '15:06 ', '16:14 ', '16:36 ', '17:06 ', '17:48 ', '19:07 ', u'\xa0', u'\xa0']
        expected =[u'FISH HOEK', '00:03 ', '04:36 ', '05:36 ', '06:34 ', '07:30 ', '08:29 ', '09:16 ', '09:40 ', '10:07 ', '10:54 ', '12:05 ', u'FISH HOEK', '13:12 ', '13:53 ', '15:06 ', '16:14 ', '16:36 ', '17:06 ', '17:48 ', '19:07 ', '', '']

        print html.strip_unprintables(row)
        self.assertEquals(
            expected,
            html.strip_unprintables(row)
        )