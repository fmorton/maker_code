from robot.hummingbird import Hummingbird
from robot.tasks import Tasks

from battle_bot_bling import bling
from battle_bot_driving import driving
from battle_bot_weapons import weapons

hummingbird = Hummingbird("A")

tasks = Tasks()

tasks.create_task(driving(hummingbird))
tasks.create_task(weapons(hummingbird))
tasks.create_task(bling(hummingbird))

tasks.run()
