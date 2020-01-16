import sys
import time
import zmq
from distri import print_board

context = zmq.Context()

fan = context.socket(zmq.REQ)
fan.bind("tcp://*:5558")

work = context.socket(zmq.PULL)
work.bind("tcp://*:5559")

work.recv_string()

while True:
    answer = work.recv_json()
    fan.send_json(answer)
    fan.recv_string()
    if answer['work']=='success':
        print_board(answer['board'])
        break