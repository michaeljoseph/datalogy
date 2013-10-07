"""
scrape: Extract HTML elements using an XPath query or CSS3 selector.

Example usage:

     curl -s http://en.wikipedia.org/wiki/List_of_sovereign_states | \
             scrape -be 'table.wikitable > tr > td > b > a'

Dependencies: lxml and optionally cssselector

Copyright (C) 2013 Jeroen Janssens
Copyright (C) 2013 Michael Joseph

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see [http://www.gnu.org/licenses/].
"""

import argparse
import sys

from lxml import etree
cssselect = None
try:
    import cssselect
except:
    pass


def html_wrap(html):
    html.insert(0, '<!DOCTYPE html>\n<html>\n<body>\n')
    html.append('</body>\n</html>\n')
    return html


def scrape(html, expression):
    if not expression.startswith('//') and cssselect:
        expression = cssselect.GenericTranslator().css_to_xpath(expression)

    document = etree.fromstring(
        html,
        parser=etree.HTMLParser(encoding='utf-8')
    )

    output = []
    for element in document.xpath(expression):
        try:
            output.append(
                etree.tostring(element).encode('utf-8') + '\n'
            )
        except IOError:
            pass

    return output


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-e', '--expression', default='*',
                        help='XPath query or CSS3 selector')
    args = parser.parse_args()

    html, expression = (
        '\n'.join(sys.stdin.readlines()),
        args.expression,
    )

    try:
        output = scrape(html, expression)
    except cssselect.SelectorError:
        parser.error('Invalid CSS selector')

    for line in output:
        try:
            sys.stdout.write(line)
            sys.stdout.flush()
        except IOError:
            pass


if __name__ == '__main__':
    exit(main())
