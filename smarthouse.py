import logging
import time
from smarthouse_temperature_sensor import Sensor
from smarthouse_lightbulb import Actuator

import common

log_format = "%(asctime)s: %(message)s"
logging.basicConfig(format=log_format, level=logging.INFO, datefmt="%H:%M:%S")

# https://realpython.com/intro-to-python-threading/

sensor = Sensor(common.TEMPERATURE_SENSOR_DID)
sensor.run()

actuator = Actuator(common.LIGHTBULB_DID)
actuator.run()


try:
    while True:
        time.sleep(1)  # Du kan sette en kort pause for å redusere CPU-bruk.
except KeyboardInterrupt:
    print("\nAvslutter etter brukerforespørsel (Ctrl+C)...")
finally:
    sensor.stop() 
    actuator.stop() # Stopper trådene på en kontrollert måte
    print("Venter på at trådene avslutter...")
    print("Program avsluttet.")




