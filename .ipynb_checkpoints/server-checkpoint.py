import grpc
from concurrent import futures
import numstore_pb2_grpc
import numstore_pb2

global dict_val={}
global dict_sum = 0

Class meow(numstore_pb2_grpc.NumStoreServicer):
    def SetNum(self,request,context):
        print(request)
        return numstore_pb2.SetNumResponse(result=3)
    def Fact(self,hello):
        return numstore_pb2.FactResponse(value=4)
    def server(self):
        server = grpc.server(futures.ThreadPoolExecutor(max_workers=4))
        numstore_pb2_grpc.add_NumStoreServicer_to_server(meow(),server)
        print('LISTENING ON PORT : 5440')
        server.add_insecure_port('[::]:5440')
        server.start()
        server.wait_for_termination()
       


