# (c) 2021 Yannic Breiting
from praktikum4.new_reader import Reader

if __name__ == '__main__':
    reader = Reader()
    g = reader.read('Karte_float.xml')
    g.dijkstra('16527615', '363215')
