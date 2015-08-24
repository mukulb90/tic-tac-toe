__author__ = 'anonymous'

from utils.rule_utils import RowRulesEngine


class Diagonal(object):
    def __init__(self, id, col_size, squares_args):
        self.id = id
        self.squares = []
        self.rule_engine = RowRulesEngine()

        if self.id == 0:
            start_index = 0
            stop_index = col_size
            step = 1
        else:
            start_index = col_size-1
            stop_index = -1
            step = -1

        for i in range(start_index, stop_index, step):
            index = i*col_size + len(self.squares)
            self.squares.append(squares_args[index])

    def run(self, *args, **kwargs):
        self.rule_engine.run(self, args, kwargs)

    def __str__(self):
        return 'Diagonal:'+str(self.squares)

    def __repr__(self):
        return self.__str__()
