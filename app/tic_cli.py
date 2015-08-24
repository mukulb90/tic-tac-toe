__author__ = 'mukul'

import sys
import os
base_dir = os.path.abspath('../')
print base_dir
sys.path.append(base_dir)

from models.board import GameBoard
from utils.exceptions_utils import PlayerWinsException, InvalidOperationException


if __name__ == '__main__':

    board = GameBoard(3, 3)
    print "Welome to tic tac toe.\n"
    player = False

    print str(board)

    while(True):
        input = raw_input("Player %d enter your choice in the format : row_number col_number <X/O>\n"%(player))
        row_number,col_num,value = input.split(' ')
        row_number = int(row_number)
        col_num = int(col_num)
        try:
            board.set(row_number-1, col_num-1, value)
        except PlayerWinsException as ex:
            print 'Player %d Wins'%(player)
            print str(ex)
            sys.exit(0)
        except InvalidOperationException as continue_exception:
            print 'Invalid input: Please stick to the rules of game'
            continue
        print str(board)
        player = not player