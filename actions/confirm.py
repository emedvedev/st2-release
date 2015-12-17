from st2actions.runners.pythonrunner import Action

__all__ = [
    'ConfirmAction'
]


class ConfirmAction(Action):
    def run(self, execution, user):

        # check the execution action ref has the correct type (st2-release.request)
        # return { 'status': 'wrong ref' }

        # date isn't +2 hours
        # return { 'status': 'too old' }

        # requester vs confirming user
        # return { 'status': 'same user' }

        # hasn't been run yet
        # return { 'status': 'duplicate' }

        return {'status': 'success', 'execution': execution, 'user': user}
