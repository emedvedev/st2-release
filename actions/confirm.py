import arrow
from st2actions.runners.pythonrunner import Action

__all__ = [
    'ConfirmAction'
]


class ConfirmAction(Action):
    def run(self, execution, user, previous):

        if execution.action.ref != 'st2-release.request':
            return {'status': 'wrong ref'}

        if arrow.get(execution.end_timestamp).replace(hours=+2) < arrow.now():
            return {'status': 'too old'}

        if execution.result.user == user:
            return {'status': 'same user'}

        for previous_execution in previous:
            if previous_execution.parameters.id == execution.id:
                return {'status': 'duplicate'}

        return {'status': 'success', 'previous': previous}
