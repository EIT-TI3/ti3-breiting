# (c) 2021 Martin Kistler

import xml.etree.ElementTree as ET
import math


def get_distance(loc1, loc2):
    lat1 = loc1[0]
    lng1 = loc1[1]

    lat2 = loc2[0]
    lng2 = loc2[1]

    degreesToRadians = (math.pi / 180)
    latrad1 = lat1 * degreesToRadians
    latrad2 = lat2 * degreesToRadians
    dlat = (lat2 - lat1) * degreesToRadians
    dlng = (lng2 - lng1) * degreesToRadians

    a = math.sin(dlat / 2) * math.sin(dlat / 2) + math.cos(latrad1) * \
    math.cos(latrad2) * math.sin(dlng / 2) * math.sin(dlng / 2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    r = 6371000

    return r * c


class NodeData:
    def __init__(self, name):
        self.name = name
        self.edges = []


class EdgeData:
    def __init__(self, name, weight, next, dtype):
        self.name = name + ' ' + next
        self.weight = str(dtype(weight))
        self.next = next


def parse(filename, dtype=int):
    tree = ET.parse(filename)
    root = tree.getroot()

    raw_nodes = {}
    raw_ways = {}

    nodes = {}
    edges = []

    for child in root:
        if child.tag.lower() == 'node':
            id = child.attrib['id']
            lat = child.attrib['lat']
            lon = child.attrib['lon']
            raw_nodes.update({id: (float(lat), float(lon))})

        elif child.tag.lower() == 'way':
            id = child.attrib['id']
            node_ids = []
            for subchild in child:
                if subchild.tag.lower() == 'nd':
                    node_ids.append(subchild.attrib['ref'])
                else:
                    if subchild.attrib['k'] == 'name':
                        name = subchild.attrib['v']
            raw_ways.update({id: {'name': name, 'raw_nodes': tuple(node_ids)}})

    for node_id in raw_nodes:
        nodes.update({node_id: NodeData(node_id)})

    for id, data in raw_ways.items():
        node_id1, node_id2 = data['raw_nodes'][0], data['raw_nodes'][1]

        node1 = raw_nodes[node_id1]
        node2 = raw_nodes[node_id2]

        weight = get_distance(node1, node2)

        e1 = EdgeData(data['name'], weight, node_id1, dtype)
        e2 = EdgeData(data['name'], weight, node_id2, dtype)
        edges += [e1, e2]

        nodes[node_id1].edges.append(e2)
        nodes[node_id2].edges.append(e1)

    return list(nodes.values()), edges


def write(filename, nodes, edges):
    root = ET.Element('map')
    for node in nodes:
        node_element = ET.SubElement(root, 'node', attrib={'name': node.name})
        for edge in node.edges:
            next_element = ET.SubElement(node_element, 'next')
            next_element.text = edge.name

    for edge in edges:
        edge_element = ET.SubElement(root, 'edge', attrib={'name': edge.name, 'weight': edge.weight})
        next_element = ET.SubElement(edge_element, 'next')
        next_element.text = edge.next

    tree = ET.ElementTree(element=root)
    ET.indent(tree)
    tree.write(filename, encoding='utf-8')


if __name__ == '__main__':
    nodes, edges = parse('raw_bremen.xml', dtype=float)
    write("Bremen.xml", nodes, edges)
