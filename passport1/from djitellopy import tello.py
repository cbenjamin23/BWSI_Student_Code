from time import time
from djitellopy import Tello
import time

tello = Tello()

tello.connect()

print(tello.get_battery())


tello.takeoff()

time.sleep(3)

tello.move_forward(100)
tello.move_left(100)
tello.move_back(100)
tello.move_right(100)

tello.land()