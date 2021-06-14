import bme680


try:
    sensor = bme680.BME680(bme680.I2C_ADDR_PRIMARY)
except (RuntimeError, IOError):
    sensor = bme680.BME680(bme680.I2C_ADDR_SECONDARY)


def tempData():
    if sensor.get_sensor_data():
        return (sensor.data.temperature, sensor.data.humidity)
