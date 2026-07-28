from logger import Logger
from storage import Storage
from viewer import LogViewer
from utils import get_timestamp
logger = Logger()
storage = Storage()

logger.start()

storage.save_event("Demo Event")

logger.stop()
from storage import Storage

class Logger:
    def __init__(self):
        self.storage = Storage()

    def log_demo_event(self, message):
        self.storage.save_event(message)
      
