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
        self.stop_event = threading.Event()

    def simulator(self):

        logging.info(f"Actuator {self.did} starting")

        while not self.stop_event.is_set():

            logging.info(f"Actuator {self.did}: {self.state.state}")

            time.sleep(common.LIGHTBULB_SIMULATOR_SLEEP_TIME)

    def client(self):

        logging.info(f"Actuator Client {self.did} starting")

        # TODO: START
        # send request to cloud service with regular intervals and
        # set state of actuator according to the received response
        
        logging.info(f"Client {self.did} finishing")
        intervall = 5
        
        while not self.stop_event.is_set():
            url = f"http://127.0.0.1:8000/smarthouse/actuator/{self.did}/current"

            response = requests.get(url)
            state = response.json()["state"]

            logging.info(f"Client {self.did} state: {state}")

            if state == "running":
                self.state = ActuatorState('True')
            elif state == "off":
                self.state = ActuatorState('False')
            print(response.json())

            time.sleep(intervall)
        
        

    def run(self):
    
        # TODO: START

        # start thread simulating physical light bulb
        sim = threading.Thread(target=self.simulator)
        sim.start()
        # start thread receiving state from the cloud
        state = threading.Thread(target=self.client)
        state.start()
        # TODO: END
    
    def stop(self):
        self.stop_event.set()



