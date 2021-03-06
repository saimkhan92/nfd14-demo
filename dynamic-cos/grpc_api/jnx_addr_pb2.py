# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: jnx_addr.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='jnx_addr.proto',
  package='jnxBase',
  syntax='proto3',
  serialized_pb=_b('\n\x0ejnx_addr.proto\x12\x07jnxBase\"F\n\tIpAddress\x12\x15\n\x0b\x61\x64\x64r_string\x18\x01 \x01(\tH\x00\x12\x14\n\naddr_bytes\x18\x02 \x01(\x0cH\x00\x42\x0c\n\nAddrFormat\"G\n\nMacAddress\x12\x15\n\x0b\x61\x64\x64r_string\x18\x01 \x01(\tH\x00\x12\x14\n\naddr_bytes\x18\x02 \x01(\x0cH\x00\x42\x0c\n\nAddrFormat*6\n\rAddressFormat\x12\x12\n\x0e\x41\x44\x44RESS_STRING\x10\x00\x12\x11\n\rADDRESS_BYTES\x10\x01*C\n\x06\x41\x66Type\x12\x12\n\x0e\x41\x46_UNSPECIFIED\x10\x00\x12\x0b\n\x07\x41\x46_INET\x10\x01\x12\x0c\n\x08\x41\x46_INET6\x10\x02\x12\n\n\x06\x41\x46_MAC\x10\x03\x62\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

_ADDRESSFORMAT = _descriptor.EnumDescriptor(
  name='AddressFormat',
  full_name='jnxBase.AddressFormat',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ADDRESS_STRING', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ADDRESS_BYTES', index=1, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=172,
  serialized_end=226,
)
_sym_db.RegisterEnumDescriptor(_ADDRESSFORMAT)

AddressFormat = enum_type_wrapper.EnumTypeWrapper(_ADDRESSFORMAT)
_AFTYPE = _descriptor.EnumDescriptor(
  name='AfType',
  full_name='jnxBase.AfType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='AF_UNSPECIFIED', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AF_INET', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AF_INET6', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AF_MAC', index=3, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=228,
  serialized_end=295,
)
_sym_db.RegisterEnumDescriptor(_AFTYPE)

AfType = enum_type_wrapper.EnumTypeWrapper(_AFTYPE)
ADDRESS_STRING = 0
ADDRESS_BYTES = 1
AF_UNSPECIFIED = 0
AF_INET = 1
AF_INET6 = 2
AF_MAC = 3



_IPADDRESS = _descriptor.Descriptor(
  name='IpAddress',
  full_name='jnxBase.IpAddress',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='addr_string', full_name='jnxBase.IpAddress.addr_string', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='addr_bytes', full_name='jnxBase.IpAddress.addr_bytes', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='AddrFormat', full_name='jnxBase.IpAddress.AddrFormat',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=27,
  serialized_end=97,
)


_MACADDRESS = _descriptor.Descriptor(
  name='MacAddress',
  full_name='jnxBase.MacAddress',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='addr_string', full_name='jnxBase.MacAddress.addr_string', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='addr_bytes', full_name='jnxBase.MacAddress.addr_bytes', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='AddrFormat', full_name='jnxBase.MacAddress.AddrFormat',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=99,
  serialized_end=170,
)

_IPADDRESS.oneofs_by_name['AddrFormat'].fields.append(
  _IPADDRESS.fields_by_name['addr_string'])
_IPADDRESS.fields_by_name['addr_string'].containing_oneof = _IPADDRESS.oneofs_by_name['AddrFormat']
_IPADDRESS.oneofs_by_name['AddrFormat'].fields.append(
  _IPADDRESS.fields_by_name['addr_bytes'])
_IPADDRESS.fields_by_name['addr_bytes'].containing_oneof = _IPADDRESS.oneofs_by_name['AddrFormat']
_MACADDRESS.oneofs_by_name['AddrFormat'].fields.append(
  _MACADDRESS.fields_by_name['addr_string'])
_MACADDRESS.fields_by_name['addr_string'].containing_oneof = _MACADDRESS.oneofs_by_name['AddrFormat']
_MACADDRESS.oneofs_by_name['AddrFormat'].fields.append(
  _MACADDRESS.fields_by_name['addr_bytes'])
_MACADDRESS.fields_by_name['addr_bytes'].containing_oneof = _MACADDRESS.oneofs_by_name['AddrFormat']
DESCRIPTOR.message_types_by_name['IpAddress'] = _IPADDRESS
DESCRIPTOR.message_types_by_name['MacAddress'] = _MACADDRESS
DESCRIPTOR.enum_types_by_name['AddressFormat'] = _ADDRESSFORMAT
DESCRIPTOR.enum_types_by_name['AfType'] = _AFTYPE

IpAddress = _reflection.GeneratedProtocolMessageType('IpAddress', (_message.Message,), dict(
  DESCRIPTOR = _IPADDRESS,
  __module__ = 'jnx_addr_pb2'
  # @@protoc_insertion_point(class_scope:jnxBase.IpAddress)
  ))
_sym_db.RegisterMessage(IpAddress)

MacAddress = _reflection.GeneratedProtocolMessageType('MacAddress', (_message.Message,), dict(
  DESCRIPTOR = _MACADDRESS,
  __module__ = 'jnx_addr_pb2'
  # @@protoc_insertion_point(class_scope:jnxBase.MacAddress)
  ))
_sym_db.RegisterMessage(MacAddress)


import grpc
from grpc.beta import implementations as beta_implementations
from grpc.beta import interfaces as beta_interfaces
from grpc.framework.common import cardinality
from grpc.framework.interfaces.face import utilities as face_utilities
# @@protoc_insertion_point(module_scope)
