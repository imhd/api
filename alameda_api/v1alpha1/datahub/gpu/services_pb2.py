# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: alameda_api/v1alpha1/datahub/gpu/services.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from alameda_api.v1alpha1.datahub.common import metrics_pb2 as alameda__api_dot_v1alpha1_dot_datahub_dot_common_dot_metrics__pb2
from alameda_api.v1alpha1.datahub.common import queries_pb2 as alameda__api_dot_v1alpha1_dot_datahub_dot_common_dot_queries__pb2
from alameda_api.v1alpha1.datahub.gpu import gpu_pb2 as alameda__api_dot_v1alpha1_dot_datahub_dot_gpu_dot_gpu__pb2
from google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='alameda_api/v1alpha1/datahub/gpu/services.proto',
  package='containersai.alameda.v1alpha1.datahub.gpu',
  syntax='proto3',
  serialized_options=_b('Z=github.com/containers-ai/api/alameda_api/v1alpha1/datahub/gpu'),
  serialized_pb=_b('\n/alameda_api/v1alpha1/datahub/gpu/services.proto\x12)containersai.alameda.v1alpha1.datahub.gpu\x1a\x31\x61lameda_api/v1alpha1/datahub/common/metrics.proto\x1a\x31\x61lameda_api/v1alpha1/datahub/common/queries.proto\x1a*alameda_api/v1alpha1/datahub/gpu/gpu.proto\x1a\x17google/rpc/status.proto\"\x8c\x01\n\x0fListGpusRequest\x12U\n\x0fquery_condition\x18\x01 \x01(\x0b\x32<.containersai.alameda.v1alpha1.datahub.common.QueryCondition\x12\x0c\n\x04host\x18\x02 \x01(\t\x12\x14\n\x0cminor_number\x18\x03 \x01(\t\"t\n\x10ListGpusResponse\x12\"\n\x06status\x18\x01 \x01(\x0b\x32\x12.google.rpc.Status\x12<\n\x04gpus\x18\x02 \x03(\x0b\x32..containersai.alameda.v1alpha1.datahub.gpu.Gpu\"\xe2\x01\n\x15ListGpuMetricsRequest\x12U\n\x0fquery_condition\x18\x01 \x01(\x0b\x32<.containersai.alameda.v1alpha1.datahub.common.QueryCondition\x12N\n\x0cmetric_types\x18\x02 \x03(\x0e\x32\x38.containersai.alameda.v1alpha1.datahub.common.MetricType\x12\x0c\n\x04host\x18\x03 \x01(\t\x12\x14\n\x0cminor_number\x18\x04 \x01(\t\"\x87\x01\n\x16ListGpuMetricsResponse\x12\"\n\x06status\x18\x01 \x01(\x0b\x32\x12.google.rpc.Status\x12I\n\x0bgpu_metrics\x18\x02 \x03(\x0b\x32\x34.containersai.alameda.v1alpha1.datahub.gpu.GpuMetric\"p\n\x1b\x43reateGpuPredictionsRequest\x12Q\n\x0fgpu_predictions\x18\x01 \x03(\x0b\x32\x38.containersai.alameda.v1alpha1.datahub.gpu.GpuPrediction\"\xd4\x01\n\x19ListGpuPredictionsRequest\x12U\n\x0fquery_condition\x18\x01 \x01(\x0b\x32<.containersai.alameda.v1alpha1.datahub.common.QueryCondition\x12\x0c\n\x04host\x18\x02 \x01(\t\x12\x14\n\x0cminor_number\x18\x03 \x01(\t\x12\x13\n\x0bgranularity\x18\x04 \x01(\x03\x12\x10\n\x08model_id\x18\x05 \x01(\t\x12\x15\n\rprediction_id\x18\x06 \x01(\t\"\x93\x01\n\x1aListGpuPredictionsResponse\x12\"\n\x06status\x18\x01 \x01(\x0b\x32\x12.google.rpc.Status\x12Q\n\x0fgpu_predictions\x18\x02 \x03(\x0b\x32\x38.containersai.alameda.v1alpha1.datahub.gpu.GpuPredictionB?Z=github.com/containers-ai/api/alameda_api/v1alpha1/datahub/gpub\x06proto3')
  ,
  dependencies=[alameda__api_dot_v1alpha1_dot_datahub_dot_common_dot_metrics__pb2.DESCRIPTOR,alameda__api_dot_v1alpha1_dot_datahub_dot_common_dot_queries__pb2.DESCRIPTOR,alameda__api_dot_v1alpha1_dot_datahub_dot_gpu_dot_gpu__pb2.DESCRIPTOR,google_dot_rpc_dot_status__pb2.DESCRIPTOR,])




_LISTGPUSREQUEST = _descriptor.Descriptor(
  name='ListGpusRequest',
  full_name='containersai.alameda.v1alpha1.datahub.gpu.ListGpusRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='query_condition', full_name='containersai.alameda.v1alpha1.datahub.gpu.ListGpusRequest.query_condition', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='host', full_name='containersai.alameda.v1alpha1.datahub.gpu.ListGpusRequest.host', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='minor_number', full_name='containersai.alameda.v1alpha1.datahub.gpu.ListGpusRequest.minor_number', index=2,
      number=3, type=9, cpp_type=9, label=1,
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
  serialized_start=266,
  serialized_end=406,
)


_LISTGPUSRESPONSE = _descriptor.Descriptor(
  name='ListGpusResponse',
  full_name='containersai.alameda.v1alpha1.datahub.gpu.ListGpusResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='containersai.alameda.v1alpha1.datahub.gpu.ListGpusResponse.status', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='gpus', full_name='containersai.alameda.v1alpha1.datahub.gpu.ListGpusResponse.gpus', index=1,
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
  serialized_start=408,
  serialized_end=524,
)


_LISTGPUMETRICSREQUEST = _descriptor.Descriptor(
  name='ListGpuMetricsRequest',
  full_name='containersai.alameda.v1alpha1.datahub.gpu.ListGpuMetricsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='query_condition', full_name='containersai.alameda.v1alpha1.datahub.gpu.ListGpuMetricsRequest.query_condition', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='metric_types', full_name='containersai.alameda.v1alpha1.datahub.gpu.ListGpuMetricsRequest.metric_types', index=1,
      number=2, type=14, cpp_type=8, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='host', full_name='containersai.alameda.v1alpha1.datahub.gpu.ListGpuMetricsRequest.host', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='minor_number', full_name='containersai.alameda.v1alpha1.datahub.gpu.ListGpuMetricsRequest.minor_number', index=3,
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
  serialized_start=527,
  serialized_end=753,
)


_LISTGPUMETRICSRESPONSE = _descriptor.Descriptor(
  name='ListGpuMetricsResponse',
  full_name='containersai.alameda.v1alpha1.datahub.gpu.ListGpuMetricsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='containersai.alameda.v1alpha1.datahub.gpu.ListGpuMetricsResponse.status', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='gpu_metrics', full_name='containersai.alameda.v1alpha1.datahub.gpu.ListGpuMetricsResponse.gpu_metrics', index=1,
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
  serialized_start=756,
  serialized_end=891,
)


_CREATEGPUPREDICTIONSREQUEST = _descriptor.Descriptor(
  name='CreateGpuPredictionsRequest',
  full_name='containersai.alameda.v1alpha1.datahub.gpu.CreateGpuPredictionsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='gpu_predictions', full_name='containersai.alameda.v1alpha1.datahub.gpu.CreateGpuPredictionsRequest.gpu_predictions', index=0,
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
  serialized_start=893,
  serialized_end=1005,
)


_LISTGPUPREDICTIONSREQUEST = _descriptor.Descriptor(
  name='ListGpuPredictionsRequest',
  full_name='containersai.alameda.v1alpha1.datahub.gpu.ListGpuPredictionsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='query_condition', full_name='containersai.alameda.v1alpha1.datahub.gpu.ListGpuPredictionsRequest.query_condition', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='host', full_name='containersai.alameda.v1alpha1.datahub.gpu.ListGpuPredictionsRequest.host', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='minor_number', full_name='containersai.alameda.v1alpha1.datahub.gpu.ListGpuPredictionsRequest.minor_number', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='granularity', full_name='containersai.alameda.v1alpha1.datahub.gpu.ListGpuPredictionsRequest.granularity', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='model_id', full_name='containersai.alameda.v1alpha1.datahub.gpu.ListGpuPredictionsRequest.model_id', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='prediction_id', full_name='containersai.alameda.v1alpha1.datahub.gpu.ListGpuPredictionsRequest.prediction_id', index=5,
      number=6, type=9, cpp_type=9, label=1,
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
  serialized_start=1008,
  serialized_end=1220,
)


_LISTGPUPREDICTIONSRESPONSE = _descriptor.Descriptor(
  name='ListGpuPredictionsResponse',
  full_name='containersai.alameda.v1alpha1.datahub.gpu.ListGpuPredictionsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='containersai.alameda.v1alpha1.datahub.gpu.ListGpuPredictionsResponse.status', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='gpu_predictions', full_name='containersai.alameda.v1alpha1.datahub.gpu.ListGpuPredictionsResponse.gpu_predictions', index=1,
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
  serialized_start=1223,
  serialized_end=1370,
)

_LISTGPUSREQUEST.fields_by_name['query_condition'].message_type = alameda__api_dot_v1alpha1_dot_datahub_dot_common_dot_queries__pb2._QUERYCONDITION
_LISTGPUSRESPONSE.fields_by_name['status'].message_type = google_dot_rpc_dot_status__pb2._STATUS
_LISTGPUSRESPONSE.fields_by_name['gpus'].message_type = alameda__api_dot_v1alpha1_dot_datahub_dot_gpu_dot_gpu__pb2._GPU
_LISTGPUMETRICSREQUEST.fields_by_name['query_condition'].message_type = alameda__api_dot_v1alpha1_dot_datahub_dot_common_dot_queries__pb2._QUERYCONDITION
_LISTGPUMETRICSREQUEST.fields_by_name['metric_types'].enum_type = alameda__api_dot_v1alpha1_dot_datahub_dot_common_dot_metrics__pb2._METRICTYPE
_LISTGPUMETRICSRESPONSE.fields_by_name['status'].message_type = google_dot_rpc_dot_status__pb2._STATUS
_LISTGPUMETRICSRESPONSE.fields_by_name['gpu_metrics'].message_type = alameda__api_dot_v1alpha1_dot_datahub_dot_gpu_dot_gpu__pb2._GPUMETRIC
_CREATEGPUPREDICTIONSREQUEST.fields_by_name['gpu_predictions'].message_type = alameda__api_dot_v1alpha1_dot_datahub_dot_gpu_dot_gpu__pb2._GPUPREDICTION
_LISTGPUPREDICTIONSREQUEST.fields_by_name['query_condition'].message_type = alameda__api_dot_v1alpha1_dot_datahub_dot_common_dot_queries__pb2._QUERYCONDITION
_LISTGPUPREDICTIONSRESPONSE.fields_by_name['status'].message_type = google_dot_rpc_dot_status__pb2._STATUS
_LISTGPUPREDICTIONSRESPONSE.fields_by_name['gpu_predictions'].message_type = alameda__api_dot_v1alpha1_dot_datahub_dot_gpu_dot_gpu__pb2._GPUPREDICTION
DESCRIPTOR.message_types_by_name['ListGpusRequest'] = _LISTGPUSREQUEST
DESCRIPTOR.message_types_by_name['ListGpusResponse'] = _LISTGPUSRESPONSE
DESCRIPTOR.message_types_by_name['ListGpuMetricsRequest'] = _LISTGPUMETRICSREQUEST
DESCRIPTOR.message_types_by_name['ListGpuMetricsResponse'] = _LISTGPUMETRICSRESPONSE
DESCRIPTOR.message_types_by_name['CreateGpuPredictionsRequest'] = _CREATEGPUPREDICTIONSREQUEST
DESCRIPTOR.message_types_by_name['ListGpuPredictionsRequest'] = _LISTGPUPREDICTIONSREQUEST
DESCRIPTOR.message_types_by_name['ListGpuPredictionsResponse'] = _LISTGPUPREDICTIONSRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ListGpusRequest = _reflection.GeneratedProtocolMessageType('ListGpusRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTGPUSREQUEST,
  '__module__' : 'alameda_api.v1alpha1.datahub.gpu.services_pb2'
  # @@protoc_insertion_point(class_scope:containersai.alameda.v1alpha1.datahub.gpu.ListGpusRequest)
  })
_sym_db.RegisterMessage(ListGpusRequest)

ListGpusResponse = _reflection.GeneratedProtocolMessageType('ListGpusResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTGPUSRESPONSE,
  '__module__' : 'alameda_api.v1alpha1.datahub.gpu.services_pb2'
  # @@protoc_insertion_point(class_scope:containersai.alameda.v1alpha1.datahub.gpu.ListGpusResponse)
  })
_sym_db.RegisterMessage(ListGpusResponse)

ListGpuMetricsRequest = _reflection.GeneratedProtocolMessageType('ListGpuMetricsRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTGPUMETRICSREQUEST,
  '__module__' : 'alameda_api.v1alpha1.datahub.gpu.services_pb2'
  # @@protoc_insertion_point(class_scope:containersai.alameda.v1alpha1.datahub.gpu.ListGpuMetricsRequest)
  })
_sym_db.RegisterMessage(ListGpuMetricsRequest)

ListGpuMetricsResponse = _reflection.GeneratedProtocolMessageType('ListGpuMetricsResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTGPUMETRICSRESPONSE,
  '__module__' : 'alameda_api.v1alpha1.datahub.gpu.services_pb2'
  # @@protoc_insertion_point(class_scope:containersai.alameda.v1alpha1.datahub.gpu.ListGpuMetricsResponse)
  })
_sym_db.RegisterMessage(ListGpuMetricsResponse)

CreateGpuPredictionsRequest = _reflection.GeneratedProtocolMessageType('CreateGpuPredictionsRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATEGPUPREDICTIONSREQUEST,
  '__module__' : 'alameda_api.v1alpha1.datahub.gpu.services_pb2'
  # @@protoc_insertion_point(class_scope:containersai.alameda.v1alpha1.datahub.gpu.CreateGpuPredictionsRequest)
  })
_sym_db.RegisterMessage(CreateGpuPredictionsRequest)

ListGpuPredictionsRequest = _reflection.GeneratedProtocolMessageType('ListGpuPredictionsRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTGPUPREDICTIONSREQUEST,
  '__module__' : 'alameda_api.v1alpha1.datahub.gpu.services_pb2'
  # @@protoc_insertion_point(class_scope:containersai.alameda.v1alpha1.datahub.gpu.ListGpuPredictionsRequest)
  })
_sym_db.RegisterMessage(ListGpuPredictionsRequest)

ListGpuPredictionsResponse = _reflection.GeneratedProtocolMessageType('ListGpuPredictionsResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTGPUPREDICTIONSRESPONSE,
  '__module__' : 'alameda_api.v1alpha1.datahub.gpu.services_pb2'
  # @@protoc_insertion_point(class_scope:containersai.alameda.v1alpha1.datahub.gpu.ListGpuPredictionsResponse)
  })
_sym_db.RegisterMessage(ListGpuPredictionsResponse)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
