import requests
import re
import arrow
import semver

from st2actions.runners.pythonrunner import Action

__all__ = [
    'LatestReleaseAction'
]

DOCS_URL = 'https://github.com/StackStorm/st2/blob/master/CHANGELOG.rst'
DATE_MATCH = r'(\d+\.\d+\.\d+) - (\w+ \d{2}, \d{4})'


class LatestReleaseAction(Action):
    def run(self):
        version, date = re.search(DATE_MATCH, requests.get(DOCS_URL).text).groups()
        return {
          'timestamp': arrow.get(date, 'MMMM DD, YYYY').replace(days=+1).timestamp,
          'current': version,
          'next': semver.bump_patch(version)
        }
