# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mypy_ext.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import descriptor_pb2 as google_dot_protobuf_dot_descriptor__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='mypy_ext.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0emypy_ext.proto\x1a google/protobuf/descriptor.proto\",\n\x0cPytypeImport\x12\x0c\n\x04type\x18\x01 \x01(\t\x12\x0e\n\x06module\x18\x02 \x01(\t:C\n\rpytype_import\x12\x1c.google.protobuf.FileOptions\x18\x91N \x03(\x0b\x32\r.PytypeImport:.\n\x06pytype\x12\x1d.google.protobuf.FieldOptions\x18\x92N \x01(\tb\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_descriptor__pb2.DESCRIPTOR,])


PYTYPE_IMPORT_FIELD_NUMBER = 10001
pytype_import = _descriptor.FieldDescriptor(
  name='pytype_import', full_name='pytype_import', index=0,
  number=10001, type=11, cpp_type=10, label=3,
  has_default_value=False, default_value=[],
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key)
PYTYPE_FIELD_NUMBER = 10002
pytype = _descriptor.FieldDescriptor(
  name='pytype', full_name='pytype', index=1,
  number=10002, type=9, cpp_type=9, label=1,
  has_default_value=False, default_value=b"".decode('utf-8'),
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key)


_PYTYPEIMPORT = _descriptor.Descriptor(
  name='PytypeImport',
  full_name='PytypeImport',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='PytypeImport.type', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='module', full_name='PytypeImport.module', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=52,
  serialized_end=96,
)

DESCRIPTOR.message_types_by_name['PytypeImport'] = _PYTYPEIMPORT
DESCRIPTOR.extensions_by_name['pytype_import'] = pytype_import
DESCRIPTOR.extensions_by_name['pytype'] = pytype
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PytypeImport = _reflection.GeneratedProtocolMessageType('PytypeImport', (_message.Message,), {
  'DESCRIPTOR' : _PYTYPEIMPORT,
  '__module__' : 'mypy_ext_pb2'
  # @@protoc_insertion_point(class_scope:PytypeImport)
  })
_sym_db.RegisterMessage(PytypeImport)

pytype_import.message_type = _PYTYPEIMPORT
google_dot_protobuf_dot_descriptor__pb2.FileOptions.RegisterExtension(pytype_import)
google_dot_protobuf_dot_descriptor__pb2.FieldOptions.RegisterExtension(pytype)

# @@protoc_insertion_point(module_scope)