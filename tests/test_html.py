from unittest2 import TestCase

from datalogy import html


class HtmlTestCase(TestCase):

    def test_parse_html_table(self):
        expected_html_table = [
            [u'first', u'first col'],
            [u'second', u'second col'],
            [u'third', u'third col']
        ]
        self.assertEquals(
            expected_html_table,
            html.parse_html_table("""
                <html>
                    <table>
                        <tr><td>first</td><td>first col</td></tr>
                        <tr><td>second</td><td>second col</td></tr>
                        <tr><td>third</td><td>third col</td></tr>
                    </table>
                </html>
            """),
        )

    def test_normalise_tabular_labelling(self):
        self.assertEquals(
            ['0116', '0118', '0120', '0124'],
            html.normalise_tabular_labelling(
                ['TRAIN NO.', '0116', '0118', '0120', 'TRAIN NO.', '0124'],
                'TRAIN NO.'
            )
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
        row = [u'\xa0FISH HOEK', '08:29 ', '09:16 ', '09:40 ',
               u'\xa0FISH HOEK', '13:12 ', '19:07 ', u'\xa0', u'\xa0']
        expected = [u'FISH HOEK', '08:29 ', '09:16 ', '09:40 ',
                    u'FISH HOEK', '13:12 ', '19:07 ', '', '']

        print html.strip_unprintables(row)
        self.assertEquals(
            expected,
            html.strip_unprintables(row)
        )
