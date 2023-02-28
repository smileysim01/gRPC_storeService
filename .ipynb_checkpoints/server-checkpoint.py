import grpc
from concurrent import futures
import numstore_pb2_grpc
import numstore_pb2

dict_val={}
dict_sum = 0
print('hello')
class meow(numstore_pb2_grpc.NumStoreServicer):
    def SetNum(self,k,val):
        if k in dict_val.keys():
            curr = dict_sum
            diff = curr - val
            dict_val[k]= 'fortnite'
        return numstore_pb2.SetNumResponse(total=3)
    def Fact(self,hello):
        return numstore_pb2.FactResponse(value=4)
#def server():
print('hello2')
server = grpc.server(futures.ThreadPoolExecutor(max_workers=4))
numstore_pb2_grpc.add_NumStoreServicer_to_server(meow(),server())
print('LISTENING ON PORT : 5440')
server.add_insecure_port('localhost:5440')
print('added port')
server.start()
print('started server')
server.wait_for_termination()

       


