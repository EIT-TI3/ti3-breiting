from graph import Graph
import xml.etree.ElementTree as ET


class Reader:

    def __init__(self):
        self.g = Graph()

    def read(self, filename):
        node_data = {}
        edge_data = {}

        tree = ET.parse(filename)
        root = tree.getroot()
        for child in root:
            if child.tag.lower() == 'node':
                try:
                    name = child.attrib['name']
                except:
                    name = None
                node = self.g.new_node(name)
                node_data.update({name: node})
            elif child.tag.lower() == 'edge':
                try:
                    edge = self.g.new_edge(child.attrib['name'], float(child.attrib['weight']))
                    edge_data.update({child.attrib['name']: edge})
                except:
                    print('Fehler in Edge-Knoten')

        root = tree.getroot()
        for child in root:
            if child.tag.lower() == 'node':
                curr_node = node_data[child.attrib['name']]
                for grandchild in child:
                    if grandchild.tag.lower() == 'next':
                        e = edge_data[grandchild.text]
                        curr_node.connect(e)
            elif child.tag.lower() == 'edge':
                curr_edge = edge_data[child.attrib['name']]
                for grandchild in child:
                    if grandchild.tag.lower() == 'next':
                        n = node_data[grandchild.text]
                        curr_edge.connect(n)

        return self.g


if __name__ == '__main__':
    reader = Reader()
    g = reader.read('Karte_float.xml')
    print(g)
