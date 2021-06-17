import bme680
import time

try:
    sensor = bme680.BME680(bme680.I2C_ADDR_PRIMARY)
except (RuntimeError, IOError):
    sensor = bme680.BME680(bme680.I2C_ADDR_SECONDARY)


def tempData():
    if sensor.get_sensor_data():
        return (sensor.data.temperature, sensor.data.humidity)

def main():

    # while True:
    #     if sensor.get_sensor_data():
    #         temperature = sensor.data.temperature


    #     if temperature >= 30 and highTemp == False:
    #         mailing.send_message("System Warning: The case temperature has reached " + str(temperature) +"C.")
    #         highTemp = True
    #     if temperature < 30:
    #         highTemp = False

    #     time.sleep(1)

if __name__ == "__main__":
    main()