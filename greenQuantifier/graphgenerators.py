        
def plotGreenGraph(name_of_location_1,name_of_location_2,graph_name = 'greengraph.png'):        
    import matplotlib
    import geofuncs as GF
    import urlfuncs as URLF
    import pngfuncs as PNGF
    import pointfuncs as PF 
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    plt.plot([PNGF.count_green_in_png(URLF.map_at(*location,zoom=10,satellite=True))
              for location in PF.location_sequence(GF.geolocate(name_of_location_1),
                                                   GF.geolocate(name_of_location_2),10)])

    title_string = ' '.join(['Greenness from',name_of_location_1,'to',name_of_location_2])
    plt.title(title_string)
    plt.savefig(graph_name)

def highlightGreenOnMap(your_location,map_name = 'green.png'):
    import urlfuncs as URLF
    import visfuncs as VF
    with open(map_name,'w') as green:
        green.write(VF.show_green_in_png(URLF.map_at(*your_location,
                                                     zoom=10,satellite=True)))

