__author__ = 'mukul'

from utils.exceptions_utils import InvalidOperationException
from utils.rule_utils import RulesEngine

class Square(RulesEngine):

    def __init__(self, id):
        self.id = id
        self.value = None

    def setValue(self, value):
        self.run()
        self.value = value

    def __str__(self):
        return str(self.value or ' ')

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return self.value == other.value

    def rule_square_already_set(self, *args, **kwargs):
        if self.value:
            raise InvalidOperationException('Invalid move')
