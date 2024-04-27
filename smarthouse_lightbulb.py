import logging
import threading
import time
import requests

from messaging import ActuatorState
import common


class Actuator:

    def __init__(self, did):
        self.did = did
        self.state = ActuatorState('False')

    def simulator(self):

        logging.info(f"Actuator {self.did} starting")

        while True:

            logging.info(f"Actuator {self.did}: {self.state.state}")

            time.sleep(common.LIGHTBULB_SIMULATOR_SLEEP_TIME)

    def client(self):

        logging.info(f"Actuator Client {self.did} starting")

        # TODO: START
        # send request to cloud service with regular intervals and
        # set state of actuator according to the received response
        
        logging.info(f"Client {self.did} finishing")
        intervall = 4
        i = 0
        while i > 8:
            url = "http://127.0.0.1:8000/smarthouse/actuator/{self.did}"

            payload = { "state": self.state }   #må passe på å sende rett type inn her on = "on" og off = "off"

            response = requests.put(url, json=payload)

            print(response.json())

            time.sleep(intervall)
            i += 1
        # TODO: END

    def run(self):

        pass
        # TODO: START

        # start thread simulating physical light bulb

        # start thread receiving state from the cloud

        # TODO: END


