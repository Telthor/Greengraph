from greengraph import Greengraph
from matplotlib import pyplot as plt
from map import Map
mygraph = Greengraph('London', 'Edinburgh')
data = mygraph.green_between(200)
plt.plot(data)
plt.show()
Map.show_green(mygraph)
