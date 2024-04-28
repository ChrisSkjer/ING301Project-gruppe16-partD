import logging
import threading
import time
import math
import requests

from messaging import SensorMeasurement
import common


class Sensor:

    def __init__(self, did):
        self.did = did
        self.measurement = SensorMeasurement('0.0')
        self.stop_event = threading.Event()

    def simulator(self):

        logging.info(f"Sensor {self.did} starting")

        while not self.stop_event.is_set():

            temp = round(math.sin(time.time() / 10) * common.TEMP_RANGE, 1)

            logging.info(f"Sensor {self.did}: {temp}")
            self.measurement.set_temperature(str(temp))

            time.sleep(common.TEMPERATURE_SENSOR_SIMULATOR_SLEEP_TIME)

    def client(self):

        logging.info(f"Sensor Client {self.did} starting")

        # TODO: START
        # send temperature to the cloud service with regular intervals
        
        intervall = 6
        url = f"http://127.0.0.1:8000/smarthouse/sensor/{self.did}/current"

        while not self.stop_event.is_set():
            payload = {
                    "timestamp": self.measurement.timestamp,
                    "value": self.measurement.value,
                    "unit": self.measurement.unit                             #denne må oppdateres med de simumerte målingene
}
            logging.info(f"Sensor Client {self.did}: {self.measurement.value}")
            response = requests.post(url, json=payload)

            print(response.json())

            time.sleep(intervall)
            
        # TODO: END

    def run(self):

        pass
        # TODO: START

        # create and start thread simulating physical temperature sensor

        simulering = threading.Thread(target=self.simulator)

        simulering.start()

        # create and start thread sending temperature to the cloud service
        klient = threading.Thread(target=self.client)
        klient.start()
        # TODO: END

    def stop(self):
        self.stop_event.set()


