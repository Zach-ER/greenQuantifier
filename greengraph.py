import geofuncs as GF
import urlfuncs as URLF
import pngfuncs as PNGF
import pointfuncs as PF
import visfuncs as VF

london_location=GF.geolocate("London")
print london_location

map_response=URLF.map_at(51.5072, -0.1275, zoom=10)
url= map_response.url
print url
print PNGF.count_green_in_png(URLF.map_at(*london_location))

### "save"
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
with open('green.png','w') as green:
    green.write(VF.show_green_in_png(URLF.map_at(*london_location,
        zoom=10,satellite=True)))

plt.plot([
    PNGF.count_green_in_png(
        URLF.map_at(*location,zoom=10,satellite=True))
          for location in PF.location_sequence(
              GF.geolocate("London"),
              GF.geolocate("Birmingham"),10)])
plt.savefig('greengraph.png')
