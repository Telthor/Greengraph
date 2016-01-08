from argparse import ArgumentParser
from greengraph import Greengraph
from matplotlib import pyplot as plt

def process():
    parser = ArgumentParser(description = 'Calculate amount of greenspace between two points')

    parser.add_argument('--beginning','-b', help = 'Starting point for greengraph')
    parser.add_argument('--to','-t', help = 'End point for green graph')
    parser.add_argument('--steps','-s', help = 'number of measurement steps between start and end')
    parser.add_argument('--out','-o', help = 'file that figure is saved as')

    arguments = parser.parse_args()

    my_graph = Greengraph(arguments.beginning, arguments.to)
    plt.plot(my_graph.green_between(arguments.steps))
    plt.show()

if __name__ == '__main__':
    process()
    
    

