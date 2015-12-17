# parse the changelog for the latest release date

import requests
import re
import arrow

from st2actions.runners.pythonrunner import Action

__all__ = [
    'LatestReleaseAction'
]

DOCS_URL = 'https://github.com/StackStorm/st2/blob/master/CHANGELOG.rst'
DATE_MATCH = r'\d+\.\d+\.\d+ - (\w+ \d{2}, \d{4})'


class LatestReleaseAction(Action):
    def run(self):
        date_string = re.search(DATE_MATCH, requests.get(DOCS_URL).text).groups()[0]
        return arrow.get(date_string, 'MMMM DD, YYYY').timestamp
