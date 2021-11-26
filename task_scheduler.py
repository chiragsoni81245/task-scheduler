import time
from datetime import datetime
import queue
from .task import Task


task_queue = queue()

class TaskScheduler:

    def __init__(self):
        self.state = "STOPED"

    def start(self):
        self.state = "RUNNING"
        while(self.state=="RUNNING"):
            next_task = task_queue.pop()

