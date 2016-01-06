from greengraph import Greengraph
from matplotlib import pyplot as plt
mygraph = Greengraph('London', 'Edinburgh')
data = mygraph.green_between(200)
plt.plot(data)
plt.show()
