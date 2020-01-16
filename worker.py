import sys
import time
import zmq
from distri import *

def solve(bo,depth):
    if depth==0:
        sink.send_json({'work':'work','board':bo})
        return False
    attemp=0
    Play=[[0,0],list(range(11))]
    find = find_empty(bo,attemp)
    while find:
        row, col= find
        attemp+=1
        temp=[]
        for i in range(1,10):
            if valid(bo, i, (row, col)):
                temp.append(i)
        if len(temp)==0:
            return False
        elif len(temp)==1:
            bo[row][col]=temp[0]
            attemp=0
        elif len(temp) < len(Play[1]):
            Play[0]=[row,col]
            Play[1]=temp
        find = find_empty(bo,attemp)
    
    if attemp==0:
        print("####################")
        print_board(bo)
        sink.send_json({'work':'success','board':bo})
        return True
    for j in Play[1]:
        board2 = [x[:] for x in bo]
        bo[Play[0][0]][Play[0][1]] = j
        if solve(bo, depth-1):
            return True
        bo=board2

context = zmq.Context()

work = context.socket(zmq.PULL)
work.connect("tcp://localhost:5557")

# Socket to send messages to
sink = context.socket(zmq.PUSH)
sink.connect("tcp://localhost:5559")

# Process tasks forever
while True:
    challenge = work.recv_json()['board']
    print_board(challenge)

    # Do the work
    solve(challenge,2)
