import zmq
from constPS import *

context = zmq.Context()
s = context.socket(zmq.SUB)
p = "tcp://" + HOST + ":" + PORT
s.connect(p)
s.setsockopt_string(zmq.SUBSCRIBE, "STATUS")

for i in range(5):
    status_msg = s.recv()
    print(bytes.decode(status_msg))
