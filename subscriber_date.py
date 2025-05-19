import zmq
from constPS import *

context = zmq.Context()
s = context.socket(zmq.SUB)
p = "tcp://" + HOST + ":" + PORT
s.connect(p)
s.setsockopt_string(zmq.SUBSCRIBE, "DATE")

for i in range(5):
    date_msg = s.recv()
    print(bytes.decode(date_msg))
