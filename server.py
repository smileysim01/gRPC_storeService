import grpc
from concurrent import futures
import numstore_pb2_grpc
import numstore_pb2

Class meow(numstore_pb2_grpc.NumStoreServicer):
    def SetNum(self,request,context):
        print(request)
        return numstore_pb2.SetNumResp(result=3)
       

server = grpc.server(futures.ThreadPoolExecutor(max_workers=4), options=[("grpc.so_reuseport", 0)])
numstore_pb2_grpc.add_NumStoreServicer_to_server(meow(),server())
print('LISTENING ON PORT : 5440')
server.add_insecure_port('localhost:5440')
server.start()
server.wait_for_termination()
