from robot.hummingbird import Hummingbird
from robot.tasks import Tasks
from robot.hummingbird_dual_motor_driver import HummingbirdDualMotorDriver

from battle_bot_bling import bling
from battle_bot_driving import driving
from battle_bot_weapons import weapons

hummingbird = HummingbirdDualMotorDriver("A")

tasks = Tasks()

tasks.create_task(
    driving(hummingbird)
)  # must be first task to wait for xbox controller
tasks.create_task(weapons(hummingbird))
tasks.create_task(bling(hummingbird))

tasks.run()
