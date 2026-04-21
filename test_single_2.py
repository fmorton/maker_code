from robot.hummingbird import Hummingbird
from time import sleep

hummingbird = Hummingbird()

for i in range(10):
    print("Running...")
    hummingbird.tri_led(1, 75, 100, 0)
    #hummingbird.tri_led(2, 50, 0, 0)
    sleep(2.0)

    hummingbird.tri_led(1, 75, 0, 100)
    sleep(2.0)

    hummingbird.tri_led(1, 0, 0, 0)
    #hummingbird.tri_led(2, 0, 0, 0)
    sleep(2.0)


