from nose.tools import assert_raises, assert_almost_equal, assert_equal
from ..greengraph import Greengraph
from ..Map import Map
from mock import patch, Mock
import geopy
import yaml
import numpy
from numpy import testing as nt
import requests
from matplotlib import image as img
from StringIO import StringIO


#ex_map = Map(1,1,satellite = True, sensor=False,zoom=10,size=(400,400))
fake_map = img.imread((open('fixtures/ex_map.png')))
with patch.object(requests, 'get') as mock_get:
    with patch.object(img, 'imread', return_value = fake_map) as mock_img:
        ex_map = Map(0, 0)


@patch.object(requests, 'get')
@patch.object(img, 'imread',return_value = fake_map)
def test_const(mock_img,mock_get):
    ex_map = Map(1,1,satellite = True, sensor=False,zoom=10,size=(400,400))
    mock_get.assert_called_with(
    "http://maps.googleapis.com/maps/api/staticmap?",
    params = {
        'sensor':'false',
        'zoom':10,
        'size':'400x400',
        'center':'1,1',
        'style':"feature:all|element:labels|visibility:off",
        'maptype':'satellite'
        }
    )

@patch.object(requests, 'get')
@patch.object(img, 'imread',return_value = fake_map)
def test_green(mock_img, mock_get):
    #ex_map = Map(1,1,satellite = True, sensor=False,zoom=10,size=(400,400))
    print ex_map.pixels
    print ex_map.image
    #All red
    ex_map.pixels[:,:,0] = 1
    ex_map.pixels[:,:,1] = 0
    ex_map.pixels[:,:,2] = 0
    assert((ex_map.green(1.1).all() == False))
    #All Green
    ex_map.pixels[:,:,0] = 0
    ex_map.pixels[:,:,1] = 1
    ex_map.pixels[:,:,2] = 0
    assert(ex_map.green(1.1).all() == True)
    #All Blue
    ex_map.pixels[:,:,0] = 0
    ex_map.pixels[:,:,1] = 0
    ex_map.pixels[:,:,2] = 1   
    assert(ex_map.green(1.1).all() == False)



@patch.object(requests, 'get')
@patch.object(img, 'imread',return_value = fake_map)
def test_count_green(mock_img, mock_get):
    #ex_map = Map(1,1,satellite = True, sensor=False,zoom=10,size=(400,400))
    #Array of four green pixels
    green_four = numpy.array([[[0,1,0],[0,1,0],[0,1,0],[0,1,0]]])
    ex_map.pixels = green_four
    assert(ex_map.count_green() == 4)

def test_show_green():
    green_map = ex_map.show_green()
    print ex_map.pixels
    green_map_array = img.imread(StringIO(green_map))[0,0,0:3]
    print green_map_array
    assert numpy.all(ex_map.pixels==green_map_array)
