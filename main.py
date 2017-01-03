import os, sys
from multiprocessing import Process
#sys.path.append(os.path.join(os.path.dirname(__file__)))
from pub_sub import PubSub
from spi_read_write import spi, start
from config import from_sub_to_mc, from_mc_to_pub
import time


def test_pub_sub():
    print("test")
    for i in range(100):
        values_to_transmit.put(i)
    print(values_to_transmit.empty())

    time.sleep(10)
    values_to_transmit.put(100000)

s = start()

def main():
    # Initializes process object, passes queue to it
    ps = PubSub(from_sub_to_mc, from_mc_to_pub)
    ps.daemon = False
    
    sa = spi(from_mc_to_pub, from_sub_to_mc, s)
    sa.daemon = False

    sa.start()
    ps.start()

    #test_pub_sub()

if __name__ == "__main__":
    main()