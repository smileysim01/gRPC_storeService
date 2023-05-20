# gRPC Store Service

Project collaborators:
rgundavarapu@wisc.edu
simran4@wisc.edu

One of the simplest storage systems records the values associated with keys, much like a Python dict, but via a service that could be shared by code running on different computers.

In this project, we've built a simple K/V store server that records number values for different string keys. Our server can use a Python dict for this purpose, but we used threads and locking for efficiency and safety. A client communicates with our server via RPC calls.

Learning objectives:

communicate between clients and servers via gRPC;

use locking for safety;

cache the results of expensive operations for efficiency;

measure performance statistics like cache hit rate and tail latency;

deploy your code in a Docker container
