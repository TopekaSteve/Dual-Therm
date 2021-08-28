from time import *
from threading import Thread


def my_box(delay_t):
    while True:
        print('...............My Box is Open: ')
        sleep(delay_t)
        print('...............My Box is Closed: ')
        sleep(delay_t)


def my_led(delay_t):
    while True:
        print('My Led is On: ')
        sleep(delay_t)
        print('My Led is Off: ')
        sleep(delay_t)


delay_box = 5
delay_led = 1
box_thread = Thread(target=my_box, args=(delay_box,))
led_thread = Thread(target=my_led, args=(delay_led,))
box_thread.daemon = True
led_thread.daemon = True
box_thread.start()
led_thread.start()
j = 0
while True:
    print(j)
    j = j + 1
    sleep(.1)
