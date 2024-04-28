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
        
        while True:
            url = f"http://127.0.0.1:8000/smarthouse/actuator/{self.did}/current"

            response = requests.get(url)
            state = response["state"]

            logging.info(f"Client {self.did} state: {state}")

            if response["state"] == "running":
                ActuatorState('True')
            elif response["state"] == "off":
                ActuatorState('False')
            print(response.json())
        
        
        

    def run(self):
    

        pass
        # TODO: START

        # start thread simulating physical light bulb
        sim = threading.Thread(target=self.simulator)
        sim.start()
        # start thread receiving state from the cloud
        state = threading.Thread(target=self.client)
        state.start()
        # TODO: END


