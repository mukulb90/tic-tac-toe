__author__ = 'mukul'


from utils.exceptions_utils import PlayerWinsException

class RulesEngine(object):

    def run(self, *args, **kwargs):
        for item in dir(self):
            if item.startswith('rule_'):
                rule = getattr(self, item)
                rule(args, kwargs)


class RowRulesEngine(RulesEngine):

    def rule_all_squares_equal(self, *args, **kwargs):
        if self.squares[0].value:
            if self.squares.count(self.squares[0]) == len(self.squares):
                raise PlayerWinsException('Rule passed :rule_all_squares_equal')
