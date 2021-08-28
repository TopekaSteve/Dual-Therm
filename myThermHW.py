from vpython import *
import numpy as np
from threading import Thread


def therm_1(disp_rate):

    piston1 = cylinder(pos=vector(3, -3.75, 0), axis=vector(0, 1, 0), radius=1, length=7, color=color.red, opacity=1)
    sphere1 = sphere(pos=vector(3, -4.5, 0), radius=1.45, color=color.red, opacity=1)
    glass_bulb = sphere(pos=vector(3, -4.5, 0), radius=1.75, color=color.white, opacity=.2)
    glass_cylinder = cylinder(pos=vector(3, -3.25, 0), axis=vector(0, 1, 0), radius=1.35, length=8, color=color.white,
                              opacity=.2)
    ticks = box(pos=vector(0, -3.25, 0), axis=vector(0, 1, 0), size=vector(.7, .1, .5), color=color.black, opacity=1)

    while True:
        for my_length in np.linspace(1, 7, 1000):
            rate(disp_rate)
            piston1.length = my_length
        for my_length in np.linspace(7, 1, 1000):
            rate(disp_rate)
            piston1.length = my_length


def therm_2(disp_rate):

    piston2 = cylinder(pos=vector(-3, -3.75, 0), axis=vector(0, 1, 0), radius=1, length=7, color=color.red, opacity=1)
    sphere2 = sphere(pos=vector(-3, -4.5, 0), radius=1.45, color=color.red, opacity=1)
    glass_bulb2 = sphere(pos=vector(-3, -4.5, 0), radius=1.75, color=color.white, opacity=.2)
    glass_cylinder2 = cylinder(pos=vector(-3, -3.25, 0), axis=vector(0, 1, 0), radius=1.35, length=8,
                               color=color.white, opacity=.2)
    ticks = box(pos=vector(0, -3.25, 0), axis=vector(0, 1, 0), size=vector(.7, .1, .5), color=color.black, opacity=1)

    while True:
        for my_length in np.linspace(1, 7, 1000):
            rate(disp_rate)
            piston2.length = my_length
        for my_length in np.linspace(7, 1, 1000):
            rate(disp_rate)
            piston2.length = my_length


rate_disp1 = 500
rate_disp2 = 250
disp1_thread = Thread(target=therm_1(rate_disp1), args=(rate_disp1,))
disp2_thread = Thread(target=therm_2(rate_disp2), args=(rate_disp2,))
disp1_thread.daemon = True
disp2_thread.daemon = True
disp1_thread.start()
disp2_thread.start()
