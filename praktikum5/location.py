from math import asin, cos, sqrt


class LocationAt:
    def __init__(self, filename):
        self._entries = None
        with open(filename) as file:
            self._entries = [tuple(float(value) for value in line.strip().split(';')) for line in file.readlines()]

    def last_timestamp(self) -> float:
        """
        Returns the last time stamp of the measured data
        Returns -1.0 if no data exists

        :return: :float:
        """
        return self._entries[-1][0] if len(self._entries) != 0 else -1.0

    def __str__(self):
        alignment = 6
        output = 'Eintraege\n'

        for entry in self._entries:
            output += f'{int(entry[0]):>{alignment}}:' \
                      + '  x: ' + f'{entry[1]:>0.3f}'.rjust(alignment) \
                      + '  y: ' + f'{entry[2]:>0.3f}'.rjust(alignment) \
                      + '  z: ' + f'{entry[3]:>0.3f}'.rjust(alignment) + '\n '

        return output

    def __search_entry(self, time: int or float or str) -> tuple[float, float, float] or None:
        output = None
        time = float(time)

        if time < self._entries[0][0]:
            output = (0.0, 0.0, 0.0)

        elif time > self._entries[-1][0]:
            pass

        else:
            for idx, entry in enumerate(self._entries):
                if time == entry[0]:
                    output = (entry[1], entry[2], entry[3])
                    break
                elif time < entry[0]:
                    output = (self._entries[idx - 1][1], self._entries[idx - 1][2], self._entries[idx - 1][3])
                    break
            else:
                entry = self._entries[-1]
                output = (entry[1], entry[2], entry[3])

        return output

    def get_roll(self, time) -> float:
        data = self.__search_entry(time)
        length = sqrt(data[0]**2 + data[1]**2 + data[2]**2) if data is not None else 0
        return asin(data[0]/(length*cos(self.get_nick(time)))) if length > 0 else 0

    def get_nick(self, time) -> float:
        data = self.__search_entry(time)
        length = sqrt(data[0]**2 + data[1]**2 + data[2]**2) if data is not None else 0
        return asin(-data[1] / length) if length > 0 else 0

