import GreenAnalysis.geofuncs as GF
import GreenAnalysis.urlfuncs as URLF
import GreenAnalysis.pngfuncs as PNGF
import GreenAnalysis.pointfuncs as PF
import GreenAnalysis.visfuncs as VF
from nose.tools import assert_raises

def test_london_coords():
    assert GF.geolocate('London') == (51.5073509, -0.1277583)

def test_empty_location():
    with assert_raises(TypeError) as exception:
        GF.geolocate('')
    
def test_url_is_returned():
    map_response=URLF.map_at(0, 0, zoom=10)
    url= map_response.url
    assert url[:4] == 'http'

def test_is_green_green():
    assert PNGF.is_green(0,1,0) is True 

def test_is_red_green():
    assert PNGF.is_green(1,0,0) is False 
        
def test_location_sequences():
    assert PF.location_sequence((0,0),(2,20),3) == [(0.0, 0.0), (1.0, 10.0), (2.0, 20.0)]
