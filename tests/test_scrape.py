from unittest2 import TestCase

from datalogy.scrape import scrape


class ScrapeTestCase(TestCase):

    def test_scrape(self):
        html = """
        <table class="wikitable"><tr><td><b>
        <a href="/wiki/Afghanistan" title="Afghanistan">Afghanistan</a></b>
        </td></tr></table>
        """

        self.assertEqual(
            ('<a href="/wiki/Afghanistan" '
             'title="Afghanistan">Afghanistan</a>\n'),
            scrape(html, 'table.wikitable > tr > td > b > a')[0]
        )
