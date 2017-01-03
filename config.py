from multiprocessing import Queue
# Global queues used for inter-process communications
# Access using main.name
broker_addr = "159.203.42.214"
from_sub_to_mc = Queue()
# logs all mqtt packets to file async
to_logger = Queue()
values_to_transmit = Queue()
# carries values from mqtt sub to SPI writer
from_mc_to_pub = Queue()
subscriptions = []