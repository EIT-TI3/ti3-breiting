# (c) 2021 Yannic Breiting
from praktikum4.new_reader import Reader

if __name__ == '__main__':
    reader = Reader()
    g = reader.read('a.xml')
    g.dijkstra('2958693613', '147042')
