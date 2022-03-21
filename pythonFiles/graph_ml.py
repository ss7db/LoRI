import igraph
import osmnx 


ameerpet = igraph.Graph.Load('manhatten.graphml')

# print(ameerpet.summary(verbosity=1))
x = ameerpet.es[0].attributes()
# x['mode'] = 'road'
print(x)
# ameerpet.es[0].update_attributes(x)
print( float(ameerpet.es[0].attributes()['maxspeed'][0:2]))

# print(ameerpet.edge_attributes())
# network from address, including only nodes within 1km along the network from the address
# G = osmnx.graph_from_address(
#     address="350 5th Ave, New York, NY",
#     dist=1000,
#     dist_type="network",
#     network_type="all",
# )

# G = osmnx.graph_from_place("Hyderabad, Telangana, India", network_type="all")

# ameerpet = igraph.Graph.Load('map_ameerpet.osm')
# print(ameerpet.summary(verbosity=1))

# x = osmnx.io.load_graphml('map_ameerpet.osm')
# x = osmnx.graph.graph_from_xml('manhatten.osm')
# osmnx.io.save_graphml(x, filepath=None, gephi=False, encoding='utf-8')