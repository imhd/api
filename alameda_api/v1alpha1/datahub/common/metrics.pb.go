// Code generated by protoc-gen-go. DO NOT EDIT.
// source: alameda_api/v1alpha1/datahub/common/metrics.proto

package common

import (
	fmt "fmt"
	proto "github.com/golang/protobuf/proto"
	timestamp "github.com/golang/protobuf/ptypes/timestamp"
	math "math"
)

// Reference imports to suppress errors if they are not otherwise used.
var _ = proto.Marshal
var _ = fmt.Errorf
var _ = math.Inf

// This is a compile-time assertion to ensure that this generated file
// is compatible with the proto package it is being compiled against.
// A compilation error at this line likely means your copy of the
// proto package needs to be updated.
const _ = proto.ProtoPackageIsVersion3 // please upgrade the proto package

//*
// Metric type. A metric may be either CPU or memory.
type MetricType int32

const (
	MetricType_METRICS_TYPE_UNDEFINED       MetricType = 0
	MetricType_CPU_USAGE_SECONDS_PERCENTAGE MetricType = 1
	MetricType_MEMORY_USAGE_BYTES           MetricType = 2
	MetricType_POWER_USAGE_WATTS            MetricType = 3
	MetricType_TEMPERATURE_CELSIUS          MetricType = 4
	MetricType_DUTY_CYCLE                   MetricType = 5
	MetricType_CURRENT_OFFSET               MetricType = 6
)

var MetricType_name = map[int32]string{
	0: "METRICS_TYPE_UNDEFINED",
	1: "CPU_USAGE_SECONDS_PERCENTAGE",
	2: "MEMORY_USAGE_BYTES",
	3: "POWER_USAGE_WATTS",
	4: "TEMPERATURE_CELSIUS",
	5: "DUTY_CYCLE",
	6: "CURRENT_OFFSET",
}

var MetricType_value = map[string]int32{
	"METRICS_TYPE_UNDEFINED":       0,
	"CPU_USAGE_SECONDS_PERCENTAGE": 1,
	"MEMORY_USAGE_BYTES":           2,
	"POWER_USAGE_WATTS":            3,
	"TEMPERATURE_CELSIUS":          4,
	"DUTY_CYCLE":                   5,
	"CURRENT_OFFSET":               6,
}

func (x MetricType) String() string {
	return proto.EnumName(MetricType_name, int32(x))
}

func (MetricType) EnumDescriptor() ([]byte, []int) {
	return fileDescriptor_0dcb68d43798345b, []int{0}
}

type ResourceName int32

const (
	ResourceName_RESOURCE_NAME_UNDEFINED ResourceName = 0
	ResourceName_CPU                     ResourceName = 1
	ResourceName_MEMORY                  ResourceName = 2
)

var ResourceName_name = map[int32]string{
	0: "RESOURCE_NAME_UNDEFINED",
	1: "CPU",
	2: "MEMORY",
}

var ResourceName_value = map[string]int32{
	"RESOURCE_NAME_UNDEFINED": 0,
	"CPU":                     1,
	"MEMORY":                  2,
}

func (x ResourceName) String() string {
	return proto.EnumName(ResourceName_name, int32(x))
}

func (ResourceName) EnumDescriptor() ([]byte, []int) {
	return fileDescriptor_0dcb68d43798345b, []int{1}
}

//*
// Represents a data point of time-series metric data
type Sample struct {
	Time                 *timestamp.Timestamp `protobuf:"bytes,1,opt,name=time,proto3" json:"time,omitempty"`
	EndTime              *timestamp.Timestamp `protobuf:"bytes,2,opt,name=end_time,json=endTime,proto3" json:"end_time,omitempty"`
	NumValue             string               `protobuf:"bytes,3,opt,name=num_value,json=numValue,proto3" json:"num_value,omitempty"`
	XXX_NoUnkeyedLiteral struct{}             `json:"-"`
	XXX_unrecognized     []byte               `json:"-"`
	XXX_sizecache        int32                `json:"-"`
}

func (m *Sample) Reset()         { *m = Sample{} }
func (m *Sample) String() string { return proto.CompactTextString(m) }
func (*Sample) ProtoMessage()    {}
func (*Sample) Descriptor() ([]byte, []int) {
	return fileDescriptor_0dcb68d43798345b, []int{0}
}

func (m *Sample) XXX_Unmarshal(b []byte) error {
	return xxx_messageInfo_Sample.Unmarshal(m, b)
}
func (m *Sample) XXX_Marshal(b []byte, deterministic bool) ([]byte, error) {
	return xxx_messageInfo_Sample.Marshal(b, m, deterministic)
}
func (m *Sample) XXX_Merge(src proto.Message) {
	xxx_messageInfo_Sample.Merge(m, src)
}
func (m *Sample) XXX_Size() int {
	return xxx_messageInfo_Sample.Size(m)
}
func (m *Sample) XXX_DiscardUnknown() {
	xxx_messageInfo_Sample.DiscardUnknown(m)
}

var xxx_messageInfo_Sample proto.InternalMessageInfo

func (m *Sample) GetTime() *timestamp.Timestamp {
	if m != nil {
		return m.Time
	}
	return nil
}

func (m *Sample) GetEndTime() *timestamp.Timestamp {
	if m != nil {
		return m.EndTime
	}
	return nil
}

func (m *Sample) GetNumValue() string {
	if m != nil {
		return m.NumValue
	}
	return ""
}

//*
// Represents a piece of metreic data
type MetricData struct {
	MetricType           MetricType `protobuf:"varint,1,opt,name=metric_type,json=metricType,proto3,enum=containersai.alameda.v1alpha1.datahub.common.MetricType" json:"metric_type,omitempty"`
	Data                 []*Sample  `protobuf:"bytes,2,rep,name=data,proto3" json:"data,omitempty"`
	Granularity          int64      `protobuf:"varint,3,opt,name=granularity,proto3" json:"granularity,omitempty"`
	XXX_NoUnkeyedLiteral struct{}   `json:"-"`
	XXX_unrecognized     []byte     `json:"-"`
	XXX_sizecache        int32      `json:"-"`
}

func (m *MetricData) Reset()         { *m = MetricData{} }
func (m *MetricData) String() string { return proto.CompactTextString(m) }
func (*MetricData) ProtoMessage()    {}
func (*MetricData) Descriptor() ([]byte, []int) {
	return fileDescriptor_0dcb68d43798345b, []int{1}
}

func (m *MetricData) XXX_Unmarshal(b []byte) error {
	return xxx_messageInfo_MetricData.Unmarshal(m, b)
}
func (m *MetricData) XXX_Marshal(b []byte, deterministic bool) ([]byte, error) {
	return xxx_messageInfo_MetricData.Marshal(b, m, deterministic)
}
func (m *MetricData) XXX_Merge(src proto.Message) {
	xxx_messageInfo_MetricData.Merge(m, src)
}
func (m *MetricData) XXX_Size() int {
	return xxx_messageInfo_MetricData.Size(m)
}
func (m *MetricData) XXX_DiscardUnknown() {
	xxx_messageInfo_MetricData.DiscardUnknown(m)
}

var xxx_messageInfo_MetricData proto.InternalMessageInfo

func (m *MetricData) GetMetricType() MetricType {
	if m != nil {
		return m.MetricType
	}
	return MetricType_METRICS_TYPE_UNDEFINED
}

func (m *MetricData) GetData() []*Sample {
	if m != nil {
		return m.Data
	}
	return nil
}

func (m *MetricData) GetGranularity() int64 {
	if m != nil {
		return m.Granularity
	}
	return 0
}

func init() {
	proto.RegisterEnum("containersai.alameda.v1alpha1.datahub.common.MetricType", MetricType_name, MetricType_value)
	proto.RegisterEnum("containersai.alameda.v1alpha1.datahub.common.ResourceName", ResourceName_name, ResourceName_value)
	proto.RegisterType((*Sample)(nil), "containersai.alameda.v1alpha1.datahub.common.Sample")
	proto.RegisterType((*MetricData)(nil), "containersai.alameda.v1alpha1.datahub.common.MetricData")
}

func init() {
	proto.RegisterFile("alameda_api/v1alpha1/datahub/common/metrics.proto", fileDescriptor_0dcb68d43798345b)
}

var fileDescriptor_0dcb68d43798345b = []byte{
	// 495 bytes of a gzipped FileDescriptorProto
	0x1f, 0x8b, 0x08, 0x00, 0x00, 0x00, 0x00, 0x00, 0x02, 0xff, 0x94, 0x93, 0xcf, 0x6e, 0xd3, 0x40,
	0x10, 0xc6, 0x71, 0x52, 0xd2, 0x76, 0x82, 0x2a, 0xb3, 0x88, 0xb6, 0x0a, 0x48, 0x44, 0x3d, 0x45,
	0x15, 0xac, 0x95, 0x00, 0x12, 0xc7, 0x26, 0xce, 0xa4, 0x44, 0xaa, 0x1d, 0x6b, 0x77, 0x4d, 0x65,
	0x2e, 0xab, 0x4d, 0xb2, 0xa4, 0x96, 0xfc, 0x4f, 0x8e, 0x5d, 0x29, 0xef, 0xc0, 0xf3, 0xf0, 0x22,
	0xbc, 0x10, 0x8a, 0x9d, 0x14, 0x38, 0x41, 0x6f, 0xde, 0xf1, 0xfc, 0x3e, 0xcf, 0xf7, 0x79, 0x16,
	0xfa, 0x2a, 0x52, 0xb1, 0x5e, 0x2a, 0xa9, 0xb2, 0xd0, 0xba, 0xef, 0xab, 0x28, 0xbb, 0x53, 0x7d,
	0x6b, 0xa9, 0x0a, 0x75, 0x57, 0xce, 0xad, 0x45, 0x1a, 0xc7, 0x69, 0x62, 0xc5, 0xba, 0xc8, 0xc3,
	0xc5, 0x9a, 0x66, 0x79, 0x5a, 0xa4, 0xe4, 0xed, 0x22, 0x4d, 0x0a, 0x15, 0x26, 0x3a, 0x5f, 0xab,
	0x90, 0xee, 0x78, 0xba, 0x67, 0xe9, 0x8e, 0xa5, 0x35, 0xdb, 0x79, 0xb3, 0x4a, 0xd3, 0x55, 0xa4,
	0xad, 0x8a, 0x9d, 0x97, 0xdf, 0xac, 0x22, 0x8c, 0xf5, 0xba, 0x50, 0x71, 0x56, 0xcb, 0x5d, 0x7c,
	0x37, 0xa0, 0xc5, 0x55, 0x9c, 0x45, 0x9a, 0x50, 0x38, 0xd8, 0xbe, 0x3d, 0x37, 0xba, 0x46, 0xaf,
	0x3d, 0xe8, 0xd0, 0x1a, 0xa5, 0x7b, 0x94, 0x8a, 0x3d, 0xca, 0xaa, 0x3e, 0xf2, 0x11, 0x8e, 0x74,
	0xb2, 0x94, 0x15, 0xd3, 0xf8, 0x27, 0x73, 0xa8, 0x93, 0xe5, 0xf6, 0x44, 0x5e, 0xc1, 0x71, 0x52,
	0xc6, 0xf2, 0x5e, 0x45, 0xa5, 0x3e, 0x6f, 0x76, 0x8d, 0xde, 0x31, 0x3b, 0x4a, 0xca, 0xf8, 0xcb,
	0xf6, 0x7c, 0xf1, 0xd3, 0x00, 0x70, 0x2a, 0xbf, 0x63, 0x55, 0x28, 0x12, 0x40, 0xbb, 0x76, 0x2f,
	0x8b, 0x4d, 0x56, 0x4f, 0x76, 0x32, 0xf8, 0x44, 0x1f, 0x13, 0x01, 0xad, 0xe5, 0xc4, 0x26, 0xd3,
	0x0c, 0xe2, 0x87, 0x67, 0xf2, 0x19, 0x0e, 0xb6, 0x8d, 0xe7, 0x8d, 0x6e, 0xb3, 0xd7, 0x1e, 0x7c,
	0x78, 0x9c, 0x66, 0x9d, 0x18, 0xab, 0x14, 0x48, 0x17, 0xda, 0xab, 0x5c, 0x25, 0x65, 0xa4, 0xf2,
	0xb0, 0xd8, 0x54, 0x96, 0x9a, 0xec, 0xcf, 0xd2, 0xe5, 0x8f, 0x07, 0x57, 0xd5, 0xa7, 0x3b, 0x70,
	0xea, 0xa0, 0x60, 0x53, 0x9b, 0x4b, 0x11, 0x78, 0x28, 0x7d, 0x77, 0x8c, 0x93, 0xa9, 0x8b, 0x63,
	0xf3, 0x09, 0xe9, 0xc2, 0x6b, 0xdb, 0xf3, 0xa5, 0xcf, 0x87, 0xd7, 0x28, 0x39, 0xda, 0x33, 0x77,
	0xcc, 0xa5, 0x87, 0xcc, 0x46, 0x57, 0x0c, 0xaf, 0xd1, 0x34, 0xc8, 0x29, 0x10, 0x07, 0x9d, 0x19,
	0x0b, 0x76, 0x4d, 0xa3, 0x40, 0x20, 0x37, 0x1b, 0xe4, 0x25, 0x3c, 0xf7, 0x66, 0xb7, 0xc8, 0x76,
	0xe5, 0xdb, 0xa1, 0x10, 0xdc, 0x6c, 0x92, 0x33, 0x78, 0x21, 0xd0, 0xf1, 0x90, 0x0d, 0x85, 0xcf,
	0x50, 0xda, 0x78, 0xc3, 0xa7, 0x3e, 0x37, 0x0f, 0xc8, 0x09, 0xc0, 0xd8, 0x17, 0x81, 0xb4, 0x03,
	0xfb, 0x06, 0xcd, 0xa7, 0x84, 0xc0, 0x89, 0xed, 0x33, 0x86, 0xae, 0x90, 0xb3, 0xc9, 0x84, 0xa3,
	0x30, 0x5b, 0x97, 0x57, 0xf0, 0x8c, 0xe9, 0x75, 0x5a, 0xe6, 0x0b, 0xed, 0xaa, 0xea, 0xdf, 0x9d,
	0x31, 0xe4, 0x33, 0x9f, 0xd9, 0x28, 0xdd, 0xa1, 0xf3, 0xf7, 0xe8, 0x87, 0xd0, 0xb4, 0x3d, 0xdf,
	0x34, 0x08, 0x40, 0xab, 0x9e, 0xd0, 0x6c, 0x8c, 0x46, 0x5f, 0xaf, 0x56, 0x61, 0xb1, 0x8b, 0xce,
	0xfa, 0x1d, 0xf2, 0x3b, 0x15, 0x5a, 0xdb, 0xa5, 0xff, 0x8f, 0x0b, 0x30, 0x6f, 0x55, 0xeb, 0xf4,
	0xfe, 0x57, 0x00, 0x00, 0x00, 0xff, 0xff, 0xe6, 0x84, 0xaf, 0xea, 0x2e, 0x03, 0x00, 0x00,
}
