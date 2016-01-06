from argparse import ArgumentParser
from greengraph import Greengraph

def process():
    parser = ArgumentParser(description = 'Calculate amount of greenspace between two points')

    parser.add_argument('--from','-f')
    parser.add_argument('--to','-t')
    parser.add_argument('--steps','-s')
    parser.add_argument('--out','-o')

