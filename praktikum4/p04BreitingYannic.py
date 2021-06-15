# (c) 2021 Yannic Breiting
from praktikum4.new_reader import Reader

if __name__ == '__main__':
    reader = Reader()
    g = reader.read('Bremen.xml')
    g.dijkstra('8579448859', '8226011340')
