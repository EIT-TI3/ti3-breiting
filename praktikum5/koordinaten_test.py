from koordinate import Kabinett, Koord2D, Koord3D
import math

if __name__ == '__main__':
    k1_2d = Koord2D(3, 4)
    print('k1_2d:', k1_2d)
    print('k1_2d: x={}, y={}'.format(k1_2d.x, k1_2d.y))

    k2_3d = Koord3D(3, 5, 1)
    print('k2_3d:', k2_3d)

    k1r_3d = k2_3d.rotate_z(-math.pi / 2)
    k2r_3d = k2_3d.rotate_x(-math.pi / 2)
    print('k1r_3d:', k1r_3d)
    print('k2r_3d:', k2r_3d)
    print('k2r_3d: x={:.2f}, y={:.2f}, z={:.2f}'.format(k2r_3d.x, k2r_3d.y, k2r_3d.z))

    k1_kabinett = Kabinett(k1_2d)
    k2_kabinett = Kabinett(k2_3d)
    k3_kabinett = Kabinett(k2_kabinett)
    k4_kabinett = Kabinett(k1_2d, z_=1.5)
    print('k1_kabinett:', k1_kabinett)
    print('k2_kabinett:', k2_kabinett)
    print('k3_kabinett:', k3_kabinett)
    print('k4_kabinett:', k4_kabinett)
