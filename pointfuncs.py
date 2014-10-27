
### "points"
import pngfuncs as PNGF
import geofuncs as GF
import urlfuncs as URLF 
from numpy import linspace
def location_sequence(start,end,steps):
  # Would actually prefer this if steps
  # were deduced from zoomlevel
  # But need projection code for that
  lats=linspace(start[0],end[0],steps)
  longs=linspace(start[1],end[1],steps)
  return zip(lats,longs)

[PNGF.count_green_in_png(URLF.map_at(*location,zoom=10,satellite=True))
            for location in location_sequence(
                GF.geolocate("London"),
                GF.geolocate("Birmingham"),
                10)]
