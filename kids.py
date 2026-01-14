import random

from robot.constant import Constant
from robot.finch import Finch
from time import sleep

finch = Finch("B")

for i in range(25):
    finch.move(Constant.FORWARD, 25, 50)
    finch.turn("L", 90, 50)
