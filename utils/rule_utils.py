__author__ = 'mukul'


from utils.exceptions_utils import PlayerWinsException

class RulesEngine(object):

    def run(self, callee, *args, **kwargs):
        for item in dir(self):
            if item.startswith('rule_'):
                rule = getattr(self, item)
                rule(callee, args, kwargs)


class RowRulesEngine(RulesEngine):

    def rule_all_squares_equal(self, callee, *args, **kwargs):
        if callee.squares[0].value:
            if callee.squares.count(callee.squares[0]) == len(callee.squares):
                raise PlayerWinsException('Rule passed :rule_all_squares_equal')
