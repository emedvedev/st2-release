import arrow
from st2actions.runners.pythonrunner import Action

__all__ = [
    'ConfirmAction'
]


class ConfirmAction(Action):
    def run(self, user, request_ref, request_timestamp, request_user, request_id):

        if request_ref != 'st2-release.request':
            return {'status': 'wrong ref'}

        if arrow.get(request_timestamp).replace(hours=+2) < arrow.now():
            return {'status': 'too old'}

        if request_user == user:
            return {'status': 'same user'}

        return {'status': 'success'}
