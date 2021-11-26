import time
from datetime import datetime

class Task:
    
    def __init__(self, name, function, *args):
        self.id = time.time()
        self.name = name
        self.__function = function
        self.__function_args = args

    def execute(self):
        self.__function(*self.__function_args)


