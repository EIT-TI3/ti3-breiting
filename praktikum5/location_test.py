import math
from location import LocationAt

if __name__ == '__main__':
    db = LocationAt('xRotFirst.csv')
    # Gib alle Eintraege formatiert aus
    print(db)
    # Ausgabe der Werte zu jeder vollen Sekunde (die ersten 10 Sekunden)
    last_timestamp = db.last_timestamp()
    print('Letzter Zeitstempel:', last_timestamp)
    time = 0
    while time <= 10000 and time <= last_timestamp:
        print('{:6}: nick:{:6.2f} roll:{:6.2f}'.format(time, db.get_nick(time) * 180 / math.pi,
                                                       db.get_roll(time) * 180 / math.pi))
        time += 1000
