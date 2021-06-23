import bme680
import time




def tempData():
    try:
        sensor = bme680.BME680(bme680.I2C_ADDR_PRIMARY)
    except (RuntimeError, IOError):
        sensor = bme680.BME680(bme680.I2C_ADDR_SECONDARY)
    if sensor.get_sensor_data():
        return (sensor.data.temperature, sensor.data.humidity)

def main():

        while True:
            highTemp = False
            temperature = tempData()[0]
            if temperature >= 30 and highTemp == False:
                print("System Warning: The case temperature has reached " + str(temperature) +"C.")
                highTemp = True
            if temperature < 30:
                highTemp = False

            time.sleep(1)

if __name__ == "__main__":
    main()