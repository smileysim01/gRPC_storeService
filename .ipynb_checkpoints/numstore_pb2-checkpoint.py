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




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0enumstore.proto\"\'\n\tSetNumReq\x12\x0b\n\x03key\x18\x02 \x01(\t\x12\r\n\x05value\x18\x01 \x01(\x05\"\x1b\n\nSetNumResp\x12\r\n\x05total\x18\x02 \x01(\x05\"\x16\n\x07\x46\x61\x63tReq\x12\x0b\n\x03key\x18\x01 \x01(\t\"5\n\x08\x46\x61\x63tResp\x12\r\n\x05value\x18\x03 \x01(\x05\x12\x0b\n\x03hit\x18\x05 \x01(\x08\x12\r\n\x05\x65rror\x18\x01 \x01(\t2J\n\x08NumStore\x12!\n\x06SetNum\x12\n.SetNumReq\x1a\x0b.SetNumResp\x12\x1b\n\x04\x46\x61\x63t\x12\x08.FactReq\x1a\t.FactRespb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'numstore_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _SETNUMREQ._serialized_start=18
  _SETNUMREQ._serialized_end=57
  _SETNUMRESP._serialized_start=59
  _SETNUMRESP._serialized_end=86
  _FACTREQ._serialized_start=88
  _FACTREQ._serialized_end=110
  _FACTRESP._serialized_start=112
  _FACTRESP._serialized_end=165
  _NUMSTORE._serialized_start=167
  _NUMSTORE._serialized_end=241
# @@protoc_insertion_point(module_scope)