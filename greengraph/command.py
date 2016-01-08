from argparse import ArgumentParser
from greengraph import Greengraph
from matplotlib import pyplot as plt

def process():
    parser = ArgumentParser(description = 'Calculate amount of greenspace between two points')

    parser.add_argument('--beginning','-b')
    parser.add_argument('--to','-t')
    parser.add_argument('--steps','-s')
    parser.add_argument('--out','-o')

    arguments = parser.parse_args()

    my_graph = Greengraph(arguments.beginning, arguments.to)
    plt.plot(my_graph.green_between(arguments.steps))
    plt.show()

if __name__ == '__main__':
    process()
    
    

