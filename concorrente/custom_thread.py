from threading import Thread
import time
import requests

class CustomThread(Thread):
    def __init__(self, args):
        Thread.__init__(self)
        self.value = None
        self.args = args
 
    def run(self):
        inicial = time.time()
        response = requests.request("GET", self.args[0], headers=self.args[1], params=self.args[2])
        final = time.time()
        self.value = final-inicial