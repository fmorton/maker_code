from time import sleep

from robot.hummingbird import Hummingbird

bird = Hummingbird()

print("1")
bird.led(1, 100)
bird.tri_led(1, 0, 0, 100)
bird.tri_led(2, 0, 0, 100)
sleep(1)

print("2")
bird.led(1, 100)
bird.tri_led(1, 0, 100, 0)
bird.tri_led(2, 0, 100, 0)
sleep(1)

print("3")
bird.led(1, 0)
bird.tri_led(1, 0, 100, 100)
bird.tri_led(2, 0, 100, 100)

print("4")
bird.led(1, 0)
bird.tri_led(1, 0, 0, 0)
bird.tri_led(2, 0, 0, 0)
