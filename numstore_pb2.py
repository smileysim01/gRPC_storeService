# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: numstore.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0enumstore.proto\"+\n\rSetNumRequest\x12\r\n\x05value\x18\x01 \x01(\x03\x12\x0b\n\x03key\x18\x02 \x01(\t\"\x1f\n\x0eSetNumResponse\x12\r\n\x05total\x18\x02 \x01(\x03\"\x1a\n\x0b\x46\x61\x63tRequest\x12\x0b\n\x03key\x18\x01 \x01(\t\"9\n\x0c\x46\x61\x63tResponse\x12\r\n\x05value\x18\x03 \x01(\x03\x12\x0b\n\x03hit\x18\x05 \x01(\x08\x12\r\n\x05\x65rror\x18\x01 \x01(\t2Z\n\x08NumStore\x12)\n\x06SetNum\x12\x0e.SetNumRequest\x1a\x0f.SetNumResponse\x12#\n\x04\x46\x61\x63t\x12\x0c.FactRequest\x1a\r.FactResponseb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'numstore_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _SETNUMREQUEST._serialized_start=18
  _SETNUMREQUEST._serialized_end=61
  _SETNUMRESPONSE._serialized_start=63
  _SETNUMRESPONSE._serialized_end=94
  _FACTREQUEST._serialized_start=96
  _FACTREQUEST._serialized_end=122
  _FACTRESPONSE._serialized_start=124
  _FACTRESPONSE._serialized_end=181
  _NUMSTORE._serialized_start=183
  _NUMSTORE._serialized_end=273
# @@protoc_insertion_point(module_scope)
