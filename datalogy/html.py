from pyquery import PyQuery as pq


def clean_table(table):
    """Removes empty rows, deletes row duplicates"""
    cleaned_table = []
    for row in table:
        row = remove_nbsp(row)
        if row and non_empty(row):
            cleaned_table.append(row)

    return cleaned_table


def non_empty(row):
    return any([cell for cell in row])


def normalise_tabular_labelling(row, marker_item):
    """Removes duplicate column labels"""
    for item in row:
        if item == marker_item:
            row.remove(item)
    return row


def parse_html_table(html):
    html_table = []
    document = pq(html)
    for row in document('table > tr'):
        row_data = []
        for cell in row.iterchildren():
            row_data.append(unicode(cell.text))
        html_table.append(row_data)

    return html_table


def pad_list(row, length, missing_value=None):
    padding = length - len(row)
    if padding:
        padding = padding * [missing_value]
        return row + padding
    return row


def remove_nbsp(row):
    return [cell for cell in row if cell and not cell == '&nbsp;']


def strip_unprintables(row):
    """Strip unprintable unicode characters"""
    return [cell.replace(u'\xa0', '') for cell in row]
