import zmq
import time
from datetime import datetime
from constPS import *  # -

context = zmq.Context()
s = context.socket(zmq.PUB)        # create a publisher socket
p = "tcp://" + HOST + ":" + PORT   # how and where to communicate
s.bind(p)                          # bind socket to the address

while True:
    time.sleep(5)  # wait every 5 seconds

    # Tópico TIME
    msg_time = str.encode("TIME " + time.asctime())
    s.send(msg_time)

    # Tópico DATE
    current_date = datetime.now().strftime("%Y-%m-%d")
    msg_date = str.encode("DATE " + current_date)
    s.send(msg_date)

    # Tópico STATUS
    msg_status = str.encode("STATUS OK")
    s.send(msg_status)

