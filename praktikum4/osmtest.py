import osmnx as ox

oxna = ox.settings.osm_xml_node_attrs
oxwa = ox.settings.osm_xml_way_attrs
oxwt = ox.settings.osm_xml_way_tags
utn = list(set(oxna))
utw = list(set(oxwa + oxwt))

ox.config(all_oneway=True, useful_tags_node=utn, useful_tags_way=utw)
G = ox.graph_from_xml('bremen-latest.osm', simplify=True)
ox.save_graph_xml(G, filepath='raw_bremen.xml')
ox.plot_graph(G)[1].plot()
