from robot.hummingbird import Hummingbird
from robot.hummingbird_l298n_dual_motor_driver import HummingbirdL298nDualMotorDriver
from robot.hummingbird_tb6612fng_dual_motor_driver import (
    HummingbirdTb6612fngDualMotorDriver,
)
from time import sleep

# hummingbird_driver = HummingbirdL298nDualMotorDriver(hummingbird)
from robot.hummingbird_dual_motor_driver import HummingbirdDualMotorDriver


class HummingbirdTb6612fngDualMotorDriver2(HummingbirdDualMotorDriver):
    def move_left_motor(self, speed):
        print("DEBUG move_left_motor", speed)
        hummingbird.tri_led(1, 50, 0, 0)
        sleep(1.0)

        print("adjust speed", speed)
        speed = self.adjust_speed_for_polarity(speed, self.left_polarity)
        print("adjust speed done", speed)

        print("self.minimum_speed is", self.minimum_speed)
        if speed == 0 or (abs(speed) < self.minimum_speed):
            print("DO NOTHING")
            self.robot.tri_led(1, 0, 0, 0)
        elif speed > 0:
            print("more than zero")
            self.robot.tri_led(1, abs(speed), 100, 0)
        else:
            print("less than zero")
            self.robot.tri_led(1, abs(speed), 0, 100)

    def move_right_motor(self, speed):
        speed = self.adjust_speed_for_polarity(speed, self.right_polarity)

        if speed == 0 or (abs(speed) < self.minimum_speed):
            self.robot.tri_led(2, 0, 0, 0)
        elif speed > 0:
            self.robot.tri_led(2, 0, 100, abs(speed))
        else:
            self.robot.tri_led(2, 100, 0, abs(speed))


hummingbird = Hummingbird()
hummingbird.tri_led(1, 50, 50, 50)
sleep(1.0)

hummingbird_driver = HummingbirdTb6612fngDualMotorDriver2(hummingbird)

hummingbird_driver.move_left_motor(40)
sleep(1.0)

hummingbird_driver.move_left_motor(-40)
sleep(1.0)

hummingbird_driver.stop()

hummingbird_driver.move_right_motor(40)
sleep(1.0)

hummingbird_driver.move_right_motor(-40)
sleep(1.0)

hummingbird_driver.stop()
