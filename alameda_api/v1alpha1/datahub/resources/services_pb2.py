# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: alameda_api/v1alpha1/datahub/resources/services.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from alameda_api.v1alpha1.datahub.common import queries_pb2 as alameda__api_dot_v1alpha1_dot_datahub_dot_common_dot_queries__pb2
from alameda_api.v1alpha1.datahub.resources import metadata_pb2 as alameda__api_dot_v1alpha1_dot_datahub_dot_resources_dot_metadata__pb2
from alameda_api.v1alpha1.datahub.resources import resources_pb2 as alameda__api_dot_v1alpha1_dot_datahub_dot_resources_dot_resources__pb2
from alameda_api.v1alpha1.datahub.resources import types_pb2 as alameda__api_dot_v1alpha1_dot_datahub_dot_resources_dot_types__pb2
from google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='alameda_api/v1alpha1/datahub/resources/services.proto',
  package='containersai.alameda.v1alpha1.datahub.resources',
  syntax='proto3',
  serialized_options=_b('ZCgithub.com/containers-ai/api/alameda_api/v1alpha1/datahub/resources'),
  serialized_pb=_b('\n5alameda_api/v1alpha1/datahub/resources/services.proto\x12/containersai.alameda.v1alpha1.datahub.resources\x1a\x31\x61lameda_api/v1alpha1/datahub/common/queries.proto\x1a\x35\x61lameda_api/v1alpha1/datahub/resources/metadata.proto\x1a\x36\x61lameda_api/v1alpha1/datahub/resources/resources.proto\x1a\x32\x61lameda_api/v1alpha1/datahub/resources/types.proto\x1a\x17google/rpc/status.proto\"W\n\x11\x43reatePodsRequest\x12\x42\n\x04pods\x18\x01 \x03(\x0b\x32\x34.containersai.alameda.v1alpha1.datahub.resources.Pod\"l\n\x18\x43reateControllersRequest\x12P\n\x0b\x63ontrollers\x18\x01 \x03(\x0b\x32;.containersai.alameda.v1alpha1.datahub.resources.Controller\"i\n\x19\x43reateAlamedaNodesRequest\x12L\n\ralameda_nodes\x18\x01 \x03(\x0b\x32\x35.containersai.alameda.v1alpha1.datahub.resources.Node\"z\n\x10ListPodsResponse\x12\"\n\x06status\x18\x01 \x01(\x0b\x32\x12.google.rpc.Status\x12\x42\n\x04pods\x18\x02 \x03(\x0b\x32\x34.containersai.alameda.v1alpha1.datahub.resources.Pod\"\x84\x02\n\x16ListAlamedaPodsRequest\x12X\n\x0fnamespaced_name\x18\x01 \x01(\x0b\x32?.containersai.alameda.v1alpha1.datahub.resources.NamespacedName\x12\x43\n\x04kind\x18\x02 \x01(\x0e\x32\x35.containersai.alameda.v1alpha1.datahub.resources.Kind\x12K\n\ntime_range\x18\x03 \x01(\x0b\x32\x37.containersai.alameda.v1alpha1.datahub.common.TimeRange\"f\n\x17ListAlamedaNodesRequest\x12K\n\ntime_range\x18\x01 \x01(\x0b\x32\x37.containersai.alameda.v1alpha1.datahub.common.TimeRange\"&\n\x10ListNodesRequest\x12\x12\n\nnode_names\x18\x01 \x03(\t\"}\n\x11ListNodesResponse\x12\"\n\x06status\x18\x01 \x01(\x0b\x32\x12.google.rpc.Status\x12\x44\n\x05nodes\x18\x02 \x03(\x0b\x32\x35.containersai.alameda.v1alpha1.datahub.resources.Node\"\xc9\x01\n\x16ListControllersRequest\x12U\n\x0fquery_condition\x18\x01 \x01(\x0b\x32<.containersai.alameda.v1alpha1.datahub.common.QueryCondition\x12X\n\x0fnamespaced_name\x18\x02 \x01(\x0b\x32?.containersai.alameda.v1alpha1.datahub.resources.NamespacedName\"\x8f\x01\n\x17ListControllersResponse\x12\"\n\x06status\x18\x01 \x01(\x0b\x32\x12.google.rpc.Status\x12P\n\x0b\x63ontrollers\x18\x02 \x03(\x0b\x32;.containersai.alameda.v1alpha1.datahub.resources.Controller\"0\n\x1aListPodsByNodeNamesRequest\x12\x12\n\nnode_names\x18\x01 \x03(\t\"W\n\x11\x44\x65letePodsRequest\x12\x42\n\x04pods\x18\x01 \x03(\x0b\x32\x34.containersai.alameda.v1alpha1.datahub.resources.Pod\"l\n\x18\x44\x65leteControllersRequest\x12P\n\x0b\x63ontrollers\x18\x01 \x03(\x0b\x32;.containersai.alameda.v1alpha1.datahub.resources.Controller\"i\n\x19\x44\x65leteAlamedaNodesRequest\x12L\n\ralameda_nodes\x18\x01 \x03(\x0b\x32\x35.containersai.alameda.v1alpha1.datahub.resources.NodeBEZCgithub.com/containers-ai/api/alameda_api/v1alpha1/datahub/resourcesb\x06proto3')
  ,
  dependencies=[alameda__api_dot_v1alpha1_dot_datahub_dot_common_dot_queries__pb2.DESCRIPTOR,alameda__api_dot_v1alpha1_dot_datahub_dot_resources_dot_metadata__pb2.DESCRIPTOR,alameda__api_dot_v1alpha1_dot_datahub_dot_resources_dot_resources__pb2.DESCRIPTOR,alameda__api_dot_v1alpha1_dot_datahub_dot_resources_dot_types__pb2.DESCRIPTOR,google_dot_rpc_dot_status__pb2.DESCRIPTOR,])




_CREATEPODSREQUEST = _descriptor.Descriptor(
  name='CreatePodsRequest',
  full_name='containersai.alameda.v1alpha1.datahub.resources.CreatePodsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pods', full_name='containersai.alameda.v1alpha1.datahub.resources.CreatePodsRequest.pods', index=0,
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
  serialized_start=345,
  serialized_end=432,
)


_CREATECONTROLLERSREQUEST = _descriptor.Descriptor(
  name='CreateControllersRequest',
  full_name='containersai.alameda.v1alpha1.datahub.resources.CreateControllersRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='controllers', full_name='containersai.alameda.v1alpha1.datahub.resources.CreateControllersRequest.controllers', index=0,
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
  serialized_start=434,
  serialized_end=542,
)


_CREATEALAMEDANODESREQUEST = _descriptor.Descriptor(
  name='CreateAlamedaNodesRequest',
  full_name='containersai.alameda.v1alpha1.datahub.resources.CreateAlamedaNodesRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='alameda_nodes', full_name='containersai.alameda.v1alpha1.datahub.resources.CreateAlamedaNodesRequest.alameda_nodes', index=0,
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
  serialized_start=544,
  serialized_end=649,
)


_LISTPODSRESPONSE = _descriptor.Descriptor(
  name='ListPodsResponse',
  full_name='containersai.alameda.v1alpha1.datahub.resources.ListPodsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='containersai.alameda.v1alpha1.datahub.resources.ListPodsResponse.status', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pods', full_name='containersai.alameda.v1alpha1.datahub.resources.ListPodsResponse.pods', index=1,
      number=2, type=11, cpp_type=10, label=3,
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
  serialized_start=651,
  serialized_end=773,
)


_LISTALAMEDAPODSREQUEST = _descriptor.Descriptor(
  name='ListAlamedaPodsRequest',
  full_name='containersai.alameda.v1alpha1.datahub.resources.ListAlamedaPodsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='namespaced_name', full_name='containersai.alameda.v1alpha1.datahub.resources.ListAlamedaPodsRequest.namespaced_name', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='kind', full_name='containersai.alameda.v1alpha1.datahub.resources.ListAlamedaPodsRequest.kind', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='time_range', full_name='containersai.alameda.v1alpha1.datahub.resources.ListAlamedaPodsRequest.time_range', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=776,
  serialized_end=1036,
)


_LISTALAMEDANODESREQUEST = _descriptor.Descriptor(
  name='ListAlamedaNodesRequest',
  full_name='containersai.alameda.v1alpha1.datahub.resources.ListAlamedaNodesRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='time_range', full_name='containersai.alameda.v1alpha1.datahub.resources.ListAlamedaNodesRequest.time_range', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=1038,
  serialized_end=1140,
)


_LISTNODESREQUEST = _descriptor.Descriptor(
  name='ListNodesRequest',
  full_name='containersai.alameda.v1alpha1.datahub.resources.ListNodesRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='node_names', full_name='containersai.alameda.v1alpha1.datahub.resources.ListNodesRequest.node_names', index=0,
      number=1, type=9, cpp_type=9, label=3,
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
  serialized_start=1142,
  serialized_end=1180,
)


_LISTNODESRESPONSE = _descriptor.Descriptor(
  name='ListNodesResponse',
  full_name='containersai.alameda.v1alpha1.datahub.resources.ListNodesResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='containersai.alameda.v1alpha1.datahub.resources.ListNodesResponse.status', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='nodes', full_name='containersai.alameda.v1alpha1.datahub.resources.ListNodesResponse.nodes', index=1,
      number=2, type=11, cpp_type=10, label=3,
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
  serialized_start=1182,
  serialized_end=1307,
)


_LISTCONTROLLERSREQUEST = _descriptor.Descriptor(
  name='ListControllersRequest',
  full_name='containersai.alameda.v1alpha1.datahub.resources.ListControllersRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='query_condition', full_name='containersai.alameda.v1alpha1.datahub.resources.ListControllersRequest.query_condition', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='namespaced_name', full_name='containersai.alameda.v1alpha1.datahub.resources.ListControllersRequest.namespaced_name', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=1310,
  serialized_end=1511,
)


_LISTCONTROLLERSRESPONSE = _descriptor.Descriptor(
  name='ListControllersResponse',
  full_name='containersai.alameda.v1alpha1.datahub.resources.ListControllersResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='containersai.alameda.v1alpha1.datahub.resources.ListControllersResponse.status', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='controllers', full_name='containersai.alameda.v1alpha1.datahub.resources.ListControllersResponse.controllers', index=1,
      number=2, type=11, cpp_type=10, label=3,
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
  serialized_start=1514,
  serialized_end=1657,
)


_LISTPODSBYNODENAMESREQUEST = _descriptor.Descriptor(
  name='ListPodsByNodeNamesRequest',
  full_name='containersai.alameda.v1alpha1.datahub.resources.ListPodsByNodeNamesRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='node_names', full_name='containersai.alameda.v1alpha1.datahub.resources.ListPodsByNodeNamesRequest.node_names', index=0,
      number=1, type=9, cpp_type=9, label=3,
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
  serialized_start=1659,
  serialized_end=1707,
)


_DELETEPODSREQUEST = _descriptor.Descriptor(
  name='DeletePodsRequest',
  full_name='containersai.alameda.v1alpha1.datahub.resources.DeletePodsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pods', full_name='containersai.alameda.v1alpha1.datahub.resources.DeletePodsRequest.pods', index=0,
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
  serialized_start=1709,
  serialized_end=1796,
)


_DELETECONTROLLERSREQUEST = _descriptor.Descriptor(
  name='DeleteControllersRequest',
  full_name='containersai.alameda.v1alpha1.datahub.resources.DeleteControllersRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='controllers', full_name='containersai.alameda.v1alpha1.datahub.resources.DeleteControllersRequest.controllers', index=0,
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
  serialized_start=1798,
  serialized_end=1906,
)


_DELETEALAMEDANODESREQUEST = _descriptor.Descriptor(
  name='DeleteAlamedaNodesRequest',
  full_name='containersai.alameda.v1alpha1.datahub.resources.DeleteAlamedaNodesRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='alameda_nodes', full_name='containersai.alameda.v1alpha1.datahub.resources.DeleteAlamedaNodesRequest.alameda_nodes', index=0,
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
  serialized_start=1908,
  serialized_end=2013,
)

_CREATEPODSREQUEST.fields_by_name['pods'].message_type = alameda__api_dot_v1alpha1_dot_datahub_dot_resources_dot_resources__pb2._POD
_CREATECONTROLLERSREQUEST.fields_by_name['controllers'].message_type = alameda__api_dot_v1alpha1_dot_datahub_dot_resources_dot_resources__pb2._CONTROLLER
_CREATEALAMEDANODESREQUEST.fields_by_name['alameda_nodes'].message_type = alameda__api_dot_v1alpha1_dot_datahub_dot_resources_dot_resources__pb2._NODE
_LISTPODSRESPONSE.fields_by_name['status'].message_type = google_dot_rpc_dot_status__pb2._STATUS
_LISTPODSRESPONSE.fields_by_name['pods'].message_type = alameda__api_dot_v1alpha1_dot_datahub_dot_resources_dot_resources__pb2._POD
_LISTALAMEDAPODSREQUEST.fields_by_name['namespaced_name'].message_type = alameda__api_dot_v1alpha1_dot_datahub_dot_resources_dot_metadata__pb2._NAMESPACEDNAME
_LISTALAMEDAPODSREQUEST.fields_by_name['kind'].enum_type = alameda__api_dot_v1alpha1_dot_datahub_dot_resources_dot_types__pb2._KIND
_LISTALAMEDAPODSREQUEST.fields_by_name['time_range'].message_type = alameda__api_dot_v1alpha1_dot_datahub_dot_common_dot_queries__pb2._TIMERANGE
_LISTALAMEDANODESREQUEST.fields_by_name['time_range'].message_type = alameda__api_dot_v1alpha1_dot_datahub_dot_common_dot_queries__pb2._TIMERANGE
_LISTNODESRESPONSE.fields_by_name['status'].message_type = google_dot_rpc_dot_status__pb2._STATUS
_LISTNODESRESPONSE.fields_by_name['nodes'].message_type = alameda__api_dot_v1alpha1_dot_datahub_dot_resources_dot_resources__pb2._NODE
_LISTCONTROLLERSREQUEST.fields_by_name['query_condition'].message_type = alameda__api_dot_v1alpha1_dot_datahub_dot_common_dot_queries__pb2._QUERYCONDITION
_LISTCONTROLLERSREQUEST.fields_by_name['namespaced_name'].message_type = alameda__api_dot_v1alpha1_dot_datahub_dot_resources_dot_metadata__pb2._NAMESPACEDNAME
_LISTCONTROLLERSRESPONSE.fields_by_name['status'].message_type = google_dot_rpc_dot_status__pb2._STATUS
_LISTCONTROLLERSRESPONSE.fields_by_name['controllers'].message_type = alameda__api_dot_v1alpha1_dot_datahub_dot_resources_dot_resources__pb2._CONTROLLER
_DELETEPODSREQUEST.fields_by_name['pods'].message_type = alameda__api_dot_v1alpha1_dot_datahub_dot_resources_dot_resources__pb2._POD
_DELETECONTROLLERSREQUEST.fields_by_name['controllers'].message_type = alameda__api_dot_v1alpha1_dot_datahub_dot_resources_dot_resources__pb2._CONTROLLER
_DELETEALAMEDANODESREQUEST.fields_by_name['alameda_nodes'].message_type = alameda__api_dot_v1alpha1_dot_datahub_dot_resources_dot_resources__pb2._NODE
DESCRIPTOR.message_types_by_name['CreatePodsRequest'] = _CREATEPODSREQUEST
DESCRIPTOR.message_types_by_name['CreateControllersRequest'] = _CREATECONTROLLERSREQUEST
DESCRIPTOR.message_types_by_name['CreateAlamedaNodesRequest'] = _CREATEALAMEDANODESREQUEST
DESCRIPTOR.message_types_by_name['ListPodsResponse'] = _LISTPODSRESPONSE
DESCRIPTOR.message_types_by_name['ListAlamedaPodsRequest'] = _LISTALAMEDAPODSREQUEST
DESCRIPTOR.message_types_by_name['ListAlamedaNodesRequest'] = _LISTALAMEDANODESREQUEST
DESCRIPTOR.message_types_by_name['ListNodesRequest'] = _LISTNODESREQUEST
DESCRIPTOR.message_types_by_name['ListNodesResponse'] = _LISTNODESRESPONSE
DESCRIPTOR.message_types_by_name['ListControllersRequest'] = _LISTCONTROLLERSREQUEST
DESCRIPTOR.message_types_by_name['ListControllersResponse'] = _LISTCONTROLLERSRESPONSE
DESCRIPTOR.message_types_by_name['ListPodsByNodeNamesRequest'] = _LISTPODSBYNODENAMESREQUEST
DESCRIPTOR.message_types_by_name['DeletePodsRequest'] = _DELETEPODSREQUEST
DESCRIPTOR.message_types_by_name['DeleteControllersRequest'] = _DELETECONTROLLERSREQUEST
DESCRIPTOR.message_types_by_name['DeleteAlamedaNodesRequest'] = _DELETEALAMEDANODESREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CreatePodsRequest = _reflection.GeneratedProtocolMessageType('CreatePodsRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATEPODSREQUEST,
  '__module__' : 'alameda_api.v1alpha1.datahub.resources.services_pb2'
  # @@protoc_insertion_point(class_scope:containersai.alameda.v1alpha1.datahub.resources.CreatePodsRequest)
  })
_sym_db.RegisterMessage(CreatePodsRequest)

CreateControllersRequest = _reflection.GeneratedProtocolMessageType('CreateControllersRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATECONTROLLERSREQUEST,
  '__module__' : 'alameda_api.v1alpha1.datahub.resources.services_pb2'
  # @@protoc_insertion_point(class_scope:containersai.alameda.v1alpha1.datahub.resources.CreateControllersRequest)
  })
_sym_db.RegisterMessage(CreateControllersRequest)

CreateAlamedaNodesRequest = _reflection.GeneratedProtocolMessageType('CreateAlamedaNodesRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATEALAMEDANODESREQUEST,
  '__module__' : 'alameda_api.v1alpha1.datahub.resources.services_pb2'
  # @@protoc_insertion_point(class_scope:containersai.alameda.v1alpha1.datahub.resources.CreateAlamedaNodesRequest)
  })
_sym_db.RegisterMessage(CreateAlamedaNodesRequest)

ListPodsResponse = _reflection.GeneratedProtocolMessageType('ListPodsResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTPODSRESPONSE,
  '__module__' : 'alameda_api.v1alpha1.datahub.resources.services_pb2'
  # @@protoc_insertion_point(class_scope:containersai.alameda.v1alpha1.datahub.resources.ListPodsResponse)
  })
_sym_db.RegisterMessage(ListPodsResponse)

ListAlamedaPodsRequest = _reflection.GeneratedProtocolMessageType('ListAlamedaPodsRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTALAMEDAPODSREQUEST,
  '__module__' : 'alameda_api.v1alpha1.datahub.resources.services_pb2'
  # @@protoc_insertion_point(class_scope:containersai.alameda.v1alpha1.datahub.resources.ListAlamedaPodsRequest)
  })
_sym_db.RegisterMessage(ListAlamedaPodsRequest)

ListAlamedaNodesRequest = _reflection.GeneratedProtocolMessageType('ListAlamedaNodesRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTALAMEDANODESREQUEST,
  '__module__' : 'alameda_api.v1alpha1.datahub.resources.services_pb2'
  # @@protoc_insertion_point(class_scope:containersai.alameda.v1alpha1.datahub.resources.ListAlamedaNodesRequest)
  })
_sym_db.RegisterMessage(ListAlamedaNodesRequest)

ListNodesRequest = _reflection.GeneratedProtocolMessageType('ListNodesRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTNODESREQUEST,
  '__module__' : 'alameda_api.v1alpha1.datahub.resources.services_pb2'
  # @@protoc_insertion_point(class_scope:containersai.alameda.v1alpha1.datahub.resources.ListNodesRequest)
  })
_sym_db.RegisterMessage(ListNodesRequest)

ListNodesResponse = _reflection.GeneratedProtocolMessageType('ListNodesResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTNODESRESPONSE,
  '__module__' : 'alameda_api.v1alpha1.datahub.resources.services_pb2'
  # @@protoc_insertion_point(class_scope:containersai.alameda.v1alpha1.datahub.resources.ListNodesResponse)
  })
_sym_db.RegisterMessage(ListNodesResponse)

ListControllersRequest = _reflection.GeneratedProtocolMessageType('ListControllersRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTCONTROLLERSREQUEST,
  '__module__' : 'alameda_api.v1alpha1.datahub.resources.services_pb2'
  # @@protoc_insertion_point(class_scope:containersai.alameda.v1alpha1.datahub.resources.ListControllersRequest)
  })
_sym_db.RegisterMessage(ListControllersRequest)

ListControllersResponse = _reflection.GeneratedProtocolMessageType('ListControllersResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTCONTROLLERSRESPONSE,
  '__module__' : 'alameda_api.v1alpha1.datahub.resources.services_pb2'
  # @@protoc_insertion_point(class_scope:containersai.alameda.v1alpha1.datahub.resources.ListControllersResponse)
  })
_sym_db.RegisterMessage(ListControllersResponse)

ListPodsByNodeNamesRequest = _reflection.GeneratedProtocolMessageType('ListPodsByNodeNamesRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTPODSBYNODENAMESREQUEST,
  '__module__' : 'alameda_api.v1alpha1.datahub.resources.services_pb2'
  # @@protoc_insertion_point(class_scope:containersai.alameda.v1alpha1.datahub.resources.ListPodsByNodeNamesRequest)
  })
_sym_db.RegisterMessage(ListPodsByNodeNamesRequest)

DeletePodsRequest = _reflection.GeneratedProtocolMessageType('DeletePodsRequest', (_message.Message,), {
  'DESCRIPTOR' : _DELETEPODSREQUEST,
  '__module__' : 'alameda_api.v1alpha1.datahub.resources.services_pb2'
  # @@protoc_insertion_point(class_scope:containersai.alameda.v1alpha1.datahub.resources.DeletePodsRequest)
  })
_sym_db.RegisterMessage(DeletePodsRequest)

DeleteControllersRequest = _reflection.GeneratedProtocolMessageType('DeleteControllersRequest', (_message.Message,), {
  'DESCRIPTOR' : _DELETECONTROLLERSREQUEST,
  '__module__' : 'alameda_api.v1alpha1.datahub.resources.services_pb2'
  # @@protoc_insertion_point(class_scope:containersai.alameda.v1alpha1.datahub.resources.DeleteControllersRequest)
  })
_sym_db.RegisterMessage(DeleteControllersRequest)

DeleteAlamedaNodesRequest = _reflection.GeneratedProtocolMessageType('DeleteAlamedaNodesRequest', (_message.Message,), {
  'DESCRIPTOR' : _DELETEALAMEDANODESREQUEST,
  '__module__' : 'alameda_api.v1alpha1.datahub.resources.services_pb2'
  # @@protoc_insertion_point(class_scope:containersai.alameda.v1alpha1.datahub.resources.DeleteAlamedaNodesRequest)
  })
_sym_db.RegisterMessage(DeleteAlamedaNodesRequest)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)