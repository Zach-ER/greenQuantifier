import geofuncs as GF
import urlfuncs as URLF
import pngfuncs as PNGF
import pointfuncs as PF
import visfuncs as VF

#function will look up somewhere of your choice, saving a greenified map and a plot.
def greenAnalyser(name_of_location = 'London'):

    your_location=GF.geolocate(name_of_location)
    #  your_location=(57.3,134.5)
    print your_location
    map_response=URLF.map_at(your_location[0], your_location[1], zoom=10)
    url= map_response.url
    print url
    print PNGF.count_green_in_png(URLF.map_at(*your_location))

### "save"
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    with open('green.png','w') as green:
        green.write(VF.show_green_in_png(URLF.map_at(*your_location,
        zoom=10,satellite=True)))

    plt.plot([
              PNGF.count_green_in_png(
                                      URLF.map_at(*location,zoom=10,satellite=True))
              for location in PF.location_sequence(
                                                   GF.geolocate("London"),
                                                   GF.geolocate("Birmingham"),10)])
    plt.savefig('greengraph.png')


greenAnalyser('Paris')