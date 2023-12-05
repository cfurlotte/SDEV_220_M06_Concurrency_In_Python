#15.1 Use multiprocessing to create three separate processes.
#Make each one wait a random number of seconds between zero and one, print the current time, and then exit.
#import modules needed
import sys as s
import time as t
import datetime as dt
import multiprocessing as mp
import random as rd

#function that takes and waits 0-1 seconds that then print the current time
def printTime():
    #wait for 0-1 seconds
    t.sleep(rd.random())
    #print date and time
    print(dt.datetime.now())
    s.exit()
#runs  the program
if __name__ == "__main__":
    #runs the process 3 times at the same time
    for n in range(3):
        #calls the function to print time
        p = mp.Process(target=printTime)
        #runs the printTime function
        p.start()

