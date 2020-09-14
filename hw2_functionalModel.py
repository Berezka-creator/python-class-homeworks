# Task: Write a program one statement long that displays
# the curvature of a sinusoid on the terminal

from math import sin,pi
from time import sleep

for i in list(
        map(lambda x: 26 + round(25*sin(x/(180/pi))),
            filter(lambda x: x%2==0, range(360*2)))):
    sleep(0.02); print("*"*int(i))


  
