from greengraph import Greengraph
from matplotlib import pyplot as plt
from map import Map

from random import randint
#mygraph = Greengraph('London', 'Edinburgh')
#data = mygraph.green_between(200)
#plt.plot(data)
#plt.show()

#London = mygraph.geolocate('London')
#print mygraph.geolocate('Verona')
#Edinburgh = mygraph.geolocate('Edinburgh')
#print mygraph.geolocate('Nairobi')[0]

#print mygraph.location_sequence(London,Edinburgh, 20)

test_map = Map(51,0, size = (2,2))
print test_map.pixels
#colors = []

#for i in range(10):
#    colors.append('%06X' % randint(0, 0xFFFFFF))
