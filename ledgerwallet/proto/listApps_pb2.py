# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: listApps.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='listApps.proto',
  package='listapps',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x0elistApps.proto\x12\x08listapps\"F\n\x03\x41pp\x12\r\n\x05\x66lags\x18\x01 \x01(\r\x12\x0c\n\x04hash\x18\x02 \x01(\x0c\x12\x14\n\x0chashCodeData\x18\x03 \x01(\x0c\x12\x0c\n\x04name\x18\x04 \x01(\t\"&\n\x07\x41ppList\x12\x1b\n\x04list\x18\x01 \x03(\x0b\x32\r.listapps.Appb\x06proto3')
)




_APP = _descriptor.Descriptor(
  name='App',
  full_name='listapps.App',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='flags', full_name='listapps.App.flags', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='hash', full_name='listapps.App.hash', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='hashCodeData', full_name='listapps.App.hashCodeData', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='listapps.App.name', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=28,
  serialized_end=98,
)


_APPLIST = _descriptor.Descriptor(
  name='AppList',
  full_name='listapps.AppList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='list', full_name='listapps.AppList.list', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=100,
  serialized_end=138,
)

_APPLIST.fields_by_name['list'].message_type = _APP
DESCRIPTOR.message_types_by_name['App'] = _APP
DESCRIPTOR.message_types_by_name['AppList'] = _APPLIST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

App = _reflection.GeneratedProtocolMessageType('App', (_message.Message,), dict(
  DESCRIPTOR = _APP,
  __module__ = 'listApps_pb2'
  # @@protoc_insertion_point(class_scope:listapps.App)
  ))
_sym_db.RegisterMessage(App)

AppList = _reflection.GeneratedProtocolMessageType('AppList', (_message.Message,), dict(
  DESCRIPTOR = _APPLIST,
  __module__ = 'listApps_pb2'
  # @@protoc_insertion_point(class_scope:listapps.AppList)
  ))
_sym_db.RegisterMessage(AppList)


# @@protoc_insertion_point(module_scope)