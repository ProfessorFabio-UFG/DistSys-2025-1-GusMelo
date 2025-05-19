import zmq
from constPS import *  # -

context = zmq.Context()
s = context.socket(zmq.SUB)
p = "tcp://" + HOST + ":" + PORT
s.connect(p)
s.setsockopt_string(zmq.SUBSCRIBE, "TIME")

for i in range(5):
    time_msg = s.recv()
    print(bytes.decode(time_msg))

