#rgundavarapu@wisc.edu
#simran4@wisc.edu
import grpc
from concurrent import futures
import numstore_pb2_grpc
import numstore_pb2
import threading
import collections
import numpy as np

thread_count=8 # 8 or 4 ????
port=sys.argv[1] # get port submitted when running this client
class my_client(threading.Thread):