import time
import schedule
from numpy import random
 
class Model(object):
    # initialzie a model
    def __init__(self, data):
        data['FRE'] = 0
        self.data = data

    ## get one French sentence randomly from the database

    def get_data(self):
        return self.data