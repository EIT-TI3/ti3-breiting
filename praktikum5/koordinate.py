from math import pi, cos, sin


class Koord2D:
    def __init__(self, x_, y_):
        self.__x = float(x_)
        self.__y = float(y_)

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    def __str__(self):
        return f'({self.x:>0.2f};{self.y:>0.2f})'


class Koord3D(Koord2D):
    def __init__(self, x_, y_, z_=0.0):
        super().__init__(x_, y_)
        self.__x = float(x_)
        self.__y = float(y_)
        self.__z = float(z_)

    @property
    def z(self):
        return self.__z

    def rotate_z(self, angle):
        coord = ((self.x + self.y * 1j) * (cos(angle) + 1j * sin(angle)))
        return Koord3D(coord.real, coord.imag, self.z)

    def rotate_x(self, angle):
        coord = ((self.y + self.z * 1j) * (cos(angle) + 1j * sin(angle)))
        return Koord3D(self.x, coord.real, coord.imag)

    def __str__(self):
        return f'({self.x:>0.2f};{self.y:>0.2f};{self.z:>0.2f})'


class Kabinett(Koord2D):
    __Zscale = 0.5
    __Angle = pi / 4

    def __init__(self, x_, y_=0.0, z_=0.0):
        self.__z = z_

        if isinstance(x_, Koord2D):
            self.__x = x_.x
            self.__y = x_.y

        else:
            self.__x = x_
            self.__y = y_

        if isinstance(x_, Koord3D):
            self.__z = x_.z

        super().__init__(self.__x, self.__y)

    @property
    def x(self):
        return self.__x - self.__Zscale * self.__z * cos(self.__Angle)

    @property
    def y(self):
        return self.__y - self.__Zscale * self.__z * sin(self.__Angle)
