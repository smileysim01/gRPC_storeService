#rgundavarapu@wisc.edu
#simran4@wisc.edu
import grpc
from concurrent import futures
import numstore_pb2_grpc
import numstore_pb2
import threading
import collections
import numpy as np
import random
import sys
import time as time

# info on creating multiple threads and managing them is taken from https://www.geeksforgeeks.org/how-to-create-a-new-thread-in-python/
thread_count=8 # 8 or 4 ????
thread_requests=100
total_reqs=0
my_threads=[]
my_threads_times=[]
hit_counter=0
port=sys.argv[1] # get port submitted when running this client

class my_client(threading.Thread):
    def __init__(self,port):
        threading.Thread.__init__(self)
        #self.thread_name = thread_name     
        self.port=port
        self.channel= grpc.insecure_channel("localhost:"+str(port))
        self.stub= numstore_pb2_grpc.NumStoreStub(self.channel)
    def run(self):
        global hit_counter,my_threads_times,total_reqs
        #print('Thread '+str(self.thread_name));
        for req in range(thread_requests):
            choice=random.choice(['SetNum', 'Fact']) # decide between setnum and fact (50/50) mix
            #print(choice)
            k = random.randint(1,100)
            if choice == 'SetNum':
                num = random.randint(1,15)
                #print(num)
                t1=time.time()
                setnumresp = self.stub.SetNum(numstore_pb2.SetNumRequest(key=str(k),value=num))
                t2=time.time()
                my_threads_times.append(t2-t1)
            else:
                #print(k)
                t1=time.time()
                resp=self.stub.Fact(numstore_pb2.FactRequest(key=str(k)))
                t2=time.time()
                my_threads_times.append(t2-t1)
                if resp.hit == True:
                    hit_counter+=1
                elif resp.error=='key does not exist,please add it using setnum':
                    #print('invalid key error')
                    total_reqs-=1 # subtract a request since its not valid, we are not using cache or even calculating the factorial,The rate only counts for calculating Fact, whether it is been calculated or derived from cache from piazza  
                total_reqs+=1
                    
for t in range(thread_count):
    t=my_client(port)
    my_threads.append(t)
    t.start()
    t.join()
            

print('The cache hit rate is : ',hit_counter/total_reqs)
print("p50  Time is:", np.percentile(my_threads_times, 50)) 
print("p99  Time is :", np.percentile(my_threads_times, 99))