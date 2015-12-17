import arrow
from st2actions.runners.pythonrunner import Action

__all__ = [
    'ConfirmAction'
]


class ConfirmAction(Action):
    def run(self, user, previous, request_ref, request_timestamp, request_user, request_id):

        if request_ref != 'st2-release.request':
            return {'status': 'wrong ref'}

        # confirmed
        if arrow.get(request_timestamp).replace(hours=+2) < arrow.now():
            return {'status': 'too old'}

        # confirmed
        # if request_user == user:
        #    return {'status': 'same user'}

        #
        for previous_execution in previous:
            print previous_execution.result
            print previous_execution.result.confirmation
            if previous_execution.parameters.id == request_id \
               and previous_execution.result.confirmation.status == 'success':
                return {'status': 'duplicate'}

        return {'status': 'success'}
