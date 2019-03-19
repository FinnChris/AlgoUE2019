#!/usr/bin/python3
#from sys import setrecursionlimit
#setrecursionlimit(1500)
import sys
from argparse import ArgumentParser
from argparse import RawDescriptionHelpFormatter

parser = ArgumentParser(
    prog='Towers of Hanoi',
    formatter_class=RawDescriptionHelpFormatter,
    epilog='''Program to calculate the optimal solution of a Tower of Hanoi game with n disks.
    \n Autor: Christian Jansen
    '''
)
parser.add_argument('-n', '--number',type=int, required=True, help='Number of disks.')
#parser.add_argument('--all', action='store_true', default=False, help="Return list of numbers until requested Fibonacci number.")

args = parser.parse_args()


count = 0

def hanoi_towers(n,from_peg, to_peg):
    global count
    if n == 1:
        print("Move disk from {} to {}".format(from_peg,to_peg))
        count += 1

    elif n > 1:
        unused_peg = 6 - from_peg - to_peg
        hanoi_towers(n - 1, from_peg, unused_peg)
        print("Move disk from {} to {}".format(from_peg, to_peg))
        hanoi_towers(n - 1, unused_peg, to_peg)
        count += 1




hanoi_towers(args.number,1,3)

print(count, file=sys.stderr)