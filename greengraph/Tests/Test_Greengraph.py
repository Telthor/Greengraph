from nose.tools import assert_raises, assert_almost_equal, assert_equal
from ..greengraph import Greengraph
from ..map import Map
from mock import patch, Mock
import geopy
import yaml
import numpy
from numpy import testing as nt
from matplotlib import image as img
import requests

ex_start = 'London'
ex_finish = 'Verona'
ex_steps = 10
#ex_graph = Greengraph(ex_start, ex_finish)
locations = yaml.load(open('fixtures/locations.yaml'))
fake_map = img.imread((open('fixtures/ex_map.png')))

with patch.object(requests, 'get') as mock_get:
    with patch.object(img, 'imread', return_value = fake_map) as mock_img:
        ex_map = Map(0, 0)

with patch.object(geopy.geocoders, 'GoogleV3') as mock_code:
    ex_graph = Greengraph(ex_start, ex_finish)
ex_graph.start = ex_start
ex_graph.end = ex_finish

@patch.object(geopy.geocoders, 'GoogleV3', autospec = True)
def test_const(mock_get):
    ex_graph = Greengraph(ex_start, ex_finish)
    assert_equal(ex_graph.start, ex_start)
    assert_equal(ex_graph.end, ex_finish)
    mock_get.assert_called_with(domain="maps.google.co.uk")

def test_geolocate():
    # This does connect to the internet, but this seems reasonable to me for this particular test
    for key in locations:
        location_data = [[0,tuple(locations[key])]]
        print location_data
        value = Mock(return_value = location_data)
        with patch.object(requests, 'get') as mock_get:
            with patch.object(geopy.geocoders.GoogleV3, 'geocode', value) as mock_code:
                data = Greengraph('ex_start','ex_finish').geolocate('London')
                print data
                assert_almost_equal(locations[key][0], data[0])
                assert_almost_equal(locations[key][1], data[1])



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

@patch.object(requests,'get')
@patch.object(img,'imread',return_value = fake_map)
def test_green_between(mock_img, mock_get):
    test_list = [0]*ex_steps
    value = 0
    test_graph = Greengraph('London','New York')
    data = test_graph.green_between(ex_steps)
    print data
    assert(test_list==data)
