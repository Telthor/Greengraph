from argparse import ArgumentParser
from greengraph import Greengraph, grapher
from matplotlib import pyplot as plt

def process():
    parser = ArgumentParser(description = 'Calculate amount of greenspace between two points')

    parser.add_argument('--beginning','-b', help = 'Starting point for greengraph')
    parser.add_argument('--to','-t', help = 'End point for green graph')
    parser.add_argument('--steps','-s', default = 10, help = 'number of measurement steps between start and end')
    parser.add_argument('--out','-o', default = False, help = 'file that figure is saved as')

    arguments = parser.parse_args()
    grapher(arguments.beginning, arguments.to, arguments.steps, arguments.out)

    
if __name__ == '__main__':
    process()
    
    

