"""
Quantum Receiver
"""


class QuantumReceiver:

    def __init__(self):

        self.detections = 0

    def receive(self,
                reflected,
                noise):

        if reflected or noise:

            self.detections += 1

            return True

        return False