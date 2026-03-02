import random

from robot.hummingbird import Hummingbird
from robot.processes import Processes
from time import sleep


def random_blinker(hummingbird):
    for _ in range(35):
        hummingbird.tri_led(
            1, random.randint(0, 100), random.randint(0, 100), random.randint(0, 100)
        )

        sleep(0.1)


def blue_blinker(hummingbird):
    for _ in range(35):
        hummingbird.tri_led(1, 0, 0, 100)

        sleep(0.1)


if __name__ == "__main__":
    hummingbird = Hummingbird("A")

    processes = Processes()

    processes.create_process(random_blinker, (hummingbird,))
    processes.create_process(blue_blinker, (hummingbird,))

    processes.run()

    hummingbird.tri_led(1, 0, 0, 0)
