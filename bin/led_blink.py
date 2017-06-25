# program to blink led
import RPi.GPIO as g
import time

g.setmode(g.BOARD)
g.setup(7, g.OUT)
for i in range(20):
    g.output(7, True)
    time.sleep(1)
    g.output(7, False)
    time.sleep(2)
