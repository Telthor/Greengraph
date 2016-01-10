from nose.tools import assert_raises, assert_almost_equal, assert_equal
from ..greengraph import Greengraph
from ..Map import Map
from mock import patch
import geopy
import yaml
import numpy
from numpy import testing as nt

ex_start = 'London'
ex_finish = 'Verona'
ex_steps = 10
ex_graph = Greengraph(ex_start, ex_finish)
locations = yaml.load(open('fixtures/locations.yaml'))


@patch.object(geopy.geocoders, 'GoogleV3', autospec = True)
def test_const(mock_get):
    ex_graph = Greengraph(ex_start, ex_finish)
    assert_equal(ex_graph.start, ex_start)
    assert_equal(ex_graph.end, ex_finish)
    mock_get.assert_called_with(domain="maps.google.co.uk")

def test_geolocate():
    # This does connect to the internet, but this seems reasonable to me for this particular test
    for key in locations:
        assert_almost_equal(locations[key], list(ex_graph.geolocate(key)))


def test_location_sequence():
    City_1 = [10,10]
    City_2 = [20,20]
    steps = 10
    array_lat = numpy.linspace(City_1[0],City_2[0],steps)
    array_lon = numpy.linspace(City_1[1],City_2[1],steps)
    array_tot = numpy.vstack([array_lat, array_lon])
    array_tot = array_tot.transpose()
    data = ex_graph.location_sequence(City_1, City_2,steps)
    assert numpy.array_equal(data, array_tot)


def test_green_between():
    
