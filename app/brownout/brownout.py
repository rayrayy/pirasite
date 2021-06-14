#!/usr/bin/env python3

import time
import os
from brownout import mailing
import datetime
import bme680




def run():
    # time.sleep(20)
    try:
        sensor = bme680.BME680(bme680.I2C_ADDR_PRIMARY)
    except (RuntimeError, IOError):
        sensor = bme680.BME680(bme680.I2C_ADDR_SECONDARY)

    current_time = datetime.datetime.now()

    with open("/opt/tinypilot/app/brownout/time.txt", "r") as f:
        last_seen = datetime.datetime.strptime(f.read(), "%Y-%m-%d %H:%M:%S")

    time_diff = str(current_time - last_seen) [:-7]

    # mailing.send_message("The power was cut out for " + time_diff + " since " + last_seen.strftime("%Y-%m-%d %H:%M:%S"))
    mailing.send_message("The power was out for " + time_diff + " since " + last_seen.strftime("%Y-%m-%d %H:%M:%S") +".")


    with open("/opt/tinypilot/app/brownout/logs.txt", "a") as logs:
        logs.write(last_seen.strftime("%Y-%m-%d %H:%M:%S") + " : " + time_diff + "\n")
        logs.flush()

    highTemp = False

    while True:
        current_time = datetime.datetime.now()

        if sensor.get_sensor_data():
            temperature = sensor.data.temperature


        if temperature >= 30 and highTemp == False:
            mailing.send_message("System Warning: The case temperature has reached " + str(temperature) +"C.")
            highTemp = True
        if temperature < 30:
            highTemp = False



    
        with open("/opt/tinypilot/app/brownout/time.txt", "w") as f:
            f.write(current_time.strftime("%Y-%m-%d %H:%M:%S"))
            f.flush()

        time.sleep(60)

if __name__ == "__main__":
    run()