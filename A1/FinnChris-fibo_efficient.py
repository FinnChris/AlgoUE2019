#!/bin/python3
from argparse import ArgumentParser
from argparse import RawDescriptionHelpFormatter
parser = ArgumentParser(
    prog='Inefficient Fibonacci Algorithm',
    formatter_class=RawDescriptionHelpFormatter,
    epilog='''Programm zur Berechnung einer Fibonaccizahl unter Verwendung eines rekursiven Ansatzes.
    \n Autor: Christian Jansen
    '''
)
parser.add_argument('-n', '--number',type=int, help='Index of the requested Fibbonacci number.')
parser.add_argument('--all', action='store_true', default=False, help="Return list of numbers until requested Fibonacci number.")


DEBUG=False
if DEBUG:
    args = parser.parse_args(['-n','7', '--all'])
    #args = parser.parse_args(['-h'])
else:
    args = parser.parse_args()

def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        n_1 = 1 #letztes Ergebnis
        n_2 = 0 #vorletztes Ergebnis
        for i in range(n-1):
            result = n_1 + n_2
            n_2 = n_1
            n_1 = result
        return result

if args.all:
    n = args.number + 1
    result_list = []
    for i in range(n):
        result = fibonacci(i)
        result_list.append(result)
    print(result_list)
else:
    result = fibonacci(args.number)
    print(result)