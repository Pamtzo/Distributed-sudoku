import zmq
import time

board = [
    [8,0,0,0,0,0,0,0,0],
    [0,0,3,6,0,0,0,0,0],
    [0,7,0,0,9,0,2,0,0],
    [0,5,0,0,0,7,0,0,0],
    [0,0,0,0,4,5,7,0,0],
    [0,0,0,1,0,0,0,3,0],
    [0,0,1,0,0,0,0,6,8],
    [0,0,8,5,0,0,0,1,0],
    [0,9,0,0,0,0,4,0,0]
]

context = zmq.Context()

# socket with workers
workers = context.socket(zmq.PUSH)
workers.bind("tcp://*:5557")

# socket with sink
sink = context.socket(zmq.REP)
sink.connect("tcp://localhost:5558")

sink2 = context.socket(zmq.PUSH)
sink2.connect("tcp://localhost:5559")

print("Press enter when workers are ready...")
_ = input()
print("sending tasks to workers")

sink2.send_string('Ok')

while True:
    workers.send_json({'board': board})
    new_board=sink.recv_json()
    sink.send_string('Ok')
    if new_board['work']=='success':
        break
    board=new_board['board']