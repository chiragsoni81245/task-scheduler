import time
from datetime import datetime
import queue
from task import Task

def worker():
    while True:  
        task:Task = yield
        task.execute()
        yield True

class WorkerPool:

    def __init__(self, size):
        self.size = size
        self.__worker_pool = []
        for i in range(size):
            self.__worker_pool.append({
                "worker": worker(),
                "state": "STOPED"
            })

    def submit_task(self, task):
        for i in range(self.size):
            if self.__worker_pool[i]["state"]!="RUNNING":
                self.__worker_pool[i]["worker"].send(None)
                self.__worker_pool[i]["worker"].send(task)
