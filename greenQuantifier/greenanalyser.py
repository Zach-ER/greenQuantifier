import geofuncs as GF
import urlfuncs as URLF
import pngfuncs as PNGF
import pointfuncs as PF
import visfuncs as VF
import graphgenerators as GG

#function will look up somewhere of your choice, saving a greenified map and a plot.
def greenAnalyser(name_of_location_1 = 'London',name_of_location_2 = 'Birmingham'):
    
    your_location=GF.geolocate(name_of_location_1)
    #  your_location=(57.3,134.5)
    print 'You entered',name_of_location_1, 'which is at', your_location 
    map_response=URLF.map_at(your_location[0], your_location[1], zoom=10)
    url= map_response.url
    print 'This link shows a map around the centre of your area:'
    print url
    print 'Printing a picture of the green locations on your map to green.png'
    GG.highlightGreenOnMap(your_location)
    print 'Printing a graph to greengraph.png'
    GG.plotGreenGraph(name_of_location_1,name_of_location_2)
    print 'Thanks for using the software!'
            
