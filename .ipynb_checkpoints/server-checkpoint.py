import grpc
from concurrent import futures
import numstore_pb2_grpc
import numstore_pb2
import threading

mylock=threading.Lock()

dict_val={}
dict_sum = 0
class meow(numstore_pb2_grpc.NumStoreServicer):
    print('meow')
    def SetNum(self,k,val):
        global dict_sum
        global dict_val
        with mylock:
            print('inside lock')
            if k.key in dict_val.keys():
                curr=dict_val[k.key]
                dict_val[k.key]=k.value
                dict_sum+=k.value-curr
            else:
                dict_val[k.key]=k.value
                dict_sum+=k.value
            #if k in (dict_val.keys()):
               # print('meow')
            #     print('inside keys')
            #     curr = dict_sum
            #     diff = curr - val
            #     dict_val[k]= 'fortnite'
            print('about to return setnum')
        return numstore_pb2.SetNumResponse(total=dict_sum)
    def Fact(self,factkey,factval):
        factorial=1
        print('inside fact')
        if factkey.key in dict_val.keys():
            print('inside if')
            print(factkey.key)
            for i in range(1,dict_val[factkey.key]+1):
                print('inside loop')
                factorial*=i
            return numstore_pb2.FactResponse(value=factorial)
        else:
            return numstore_pb2.FactResponse(error='key does not exist')
        print('exiting from fact')
    
def server():  
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=4))
    numstore_pb2_grpc.add_NumStoreServicer_to_server(meow(),server)
    print('LISTENING ON PORT : 5440')
    server.add_insecure_port('localhost:5440')
    print('added port')
    server.start()
    server.wait_for_termination()
    
server()

       


