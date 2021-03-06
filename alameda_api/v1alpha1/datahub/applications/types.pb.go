// Code generated by protoc-gen-go. DO NOT EDIT.
// source: alameda_api/v1alpha1/datahub/applications/types.proto

package applications

import (
	fmt "fmt"
	common "github.com/containers-ai/api/alameda_api/v1alpha1/datahub/common"
	schemas "github.com/containers-ai/api/alameda_api/v1alpha1/datahub/schemas"
	proto "github.com/golang/protobuf/proto"
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

type Application struct {
	SchemaMeta           *schemas.SchemaMeta `protobuf:"bytes,1,opt,name=schema_meta,json=schemaMeta,proto3" json:"schema_meta,omitempty"`
	ApplicationData      []*ApplicationData  `protobuf:"bytes,2,rep,name=application_data,json=applicationData,proto3" json:"application_data,omitempty"`
	XXX_NoUnkeyedLiteral struct{}            `json:"-"`
	XXX_unrecognized     []byte              `json:"-"`
	XXX_sizecache        int32               `json:"-"`
}

func (m *Application) Reset()         { *m = Application{} }
func (m *Application) String() string { return proto.CompactTextString(m) }
func (*Application) ProtoMessage()    {}
func (*Application) Descriptor() ([]byte, []int) {
	return fileDescriptor_f129145bbe587212, []int{0}
}

func (m *Application) XXX_Unmarshal(b []byte) error {
	return xxx_messageInfo_Application.Unmarshal(m, b)
}
func (m *Application) XXX_Marshal(b []byte, deterministic bool) ([]byte, error) {
	return xxx_messageInfo_Application.Marshal(b, m, deterministic)
}
func (m *Application) XXX_Merge(src proto.Message) {
	xxx_messageInfo_Application.Merge(m, src)
}
func (m *Application) XXX_Size() int {
	return xxx_messageInfo_Application.Size(m)
}
func (m *Application) XXX_DiscardUnknown() {
	xxx_messageInfo_Application.DiscardUnknown(m)
}

var xxx_messageInfo_Application proto.InternalMessageInfo

func (m *Application) GetSchemaMeta() *schemas.SchemaMeta {
	if m != nil {
		return m.SchemaMeta
	}
	return nil
}

func (m *Application) GetApplicationData() []*ApplicationData {
	if m != nil {
		return m.ApplicationData
	}
	return nil
}

type ApplicationData struct {
	Measurement          string           `protobuf:"bytes,1,opt,name=measurement,proto3" json:"measurement,omitempty"`
	ReadData             *common.ReadData `protobuf:"bytes,2,opt,name=read_data,json=readData,proto3" json:"read_data,omitempty"`
	XXX_NoUnkeyedLiteral struct{}         `json:"-"`
	XXX_unrecognized     []byte           `json:"-"`
	XXX_sizecache        int32            `json:"-"`
}

func (m *ApplicationData) Reset()         { *m = ApplicationData{} }
func (m *ApplicationData) String() string { return proto.CompactTextString(m) }
func (*ApplicationData) ProtoMessage()    {}
func (*ApplicationData) Descriptor() ([]byte, []int) {
	return fileDescriptor_f129145bbe587212, []int{1}
}

func (m *ApplicationData) XXX_Unmarshal(b []byte) error {
	return xxx_messageInfo_ApplicationData.Unmarshal(m, b)
}
func (m *ApplicationData) XXX_Marshal(b []byte, deterministic bool) ([]byte, error) {
	return xxx_messageInfo_ApplicationData.Marshal(b, m, deterministic)
}
func (m *ApplicationData) XXX_Merge(src proto.Message) {
	xxx_messageInfo_ApplicationData.Merge(m, src)
}
func (m *ApplicationData) XXX_Size() int {
	return xxx_messageInfo_ApplicationData.Size(m)
}
func (m *ApplicationData) XXX_DiscardUnknown() {
	xxx_messageInfo_ApplicationData.DiscardUnknown(m)
}

var xxx_messageInfo_ApplicationData proto.InternalMessageInfo

func (m *ApplicationData) GetMeasurement() string {
	if m != nil {
		return m.Measurement
	}
	return ""
}

func (m *ApplicationData) GetReadData() *common.ReadData {
	if m != nil {
		return m.ReadData
	}
	return nil
}

func init() {
	proto.RegisterType((*Application)(nil), "containersai.alameda.v1alpha1.datahub.applications.Application")
	proto.RegisterType((*ApplicationData)(nil), "containersai.alameda.v1alpha1.datahub.applications.ApplicationData")
}

func init() {
	proto.RegisterFile("alameda_api/v1alpha1/datahub/applications/types.proto", fileDescriptor_f129145bbe587212)
}

var fileDescriptor_f129145bbe587212 = []byte{
	// 290 bytes of a gzipped FileDescriptorProto
	0x1f, 0x8b, 0x08, 0x00, 0x00, 0x00, 0x00, 0x00, 0x02, 0xff, 0x94, 0x92, 0xcd, 0x4a, 0xc3, 0x40,
	0x14, 0x85, 0x89, 0x82, 0xd8, 0xc9, 0xa2, 0x92, 0x55, 0xe9, 0x2a, 0x74, 0xd5, 0x8d, 0x33, 0x26,
	0xa2, 0xe0, 0xd2, 0x1f, 0xc4, 0x8d, 0x9b, 0x74, 0xd7, 0x4d, 0x38, 0x4d, 0x06, 0x33, 0x90, 0xf9,
	0x61, 0x66, 0xaa, 0xf8, 0x06, 0xbe, 0xa2, 0x6f, 0x23, 0xf9, 0xa9, 0x4d, 0x5d, 0x94, 0xb8, 0xca,
	0xe5, 0x72, 0xcf, 0x3d, 0xdf, 0xcd, 0x19, 0x72, 0x83, 0x1a, 0x92, 0x97, 0xc8, 0x61, 0x04, 0x7b,
	0x4f, 0x50, 0x9b, 0x0a, 0x09, 0x2b, 0xe1, 0x51, 0x6d, 0x37, 0x0c, 0xc6, 0xd4, 0xa2, 0x80, 0x17,
	0x5a, 0x39, 0xe6, 0x3f, 0x0d, 0x77, 0xd4, 0x58, 0xed, 0x75, 0x94, 0x16, 0x5a, 0x79, 0x08, 0xc5,
	0xad, 0x83, 0xa0, 0xfd, 0x0e, 0xba, 0xd3, 0xd3, 0x5e, 0x4f, 0x87, 0xfa, 0x79, 0x72, 0xd4, 0xaa,
	0xd0, 0x52, 0x6a, 0xc5, 0x2c, 0x3e, 0x9a, 0x4e, 0x67, 0x33, 0xbf, 0x3a, 0x2a, 0x71, 0x45, 0xc5,
	0x25, 0x0e, 0xc0, 0x16, 0xdf, 0x01, 0x09, 0xef, 0xf7, 0xae, 0xd1, 0x9a, 0x84, 0xdd, 0x58, 0x2e,
	0xb9, 0xc7, 0x2c, 0x88, 0x83, 0x65, 0x98, 0xde, 0xd1, 0x71, 0xf8, 0xbd, 0x01, 0x5d, 0xb5, 0xdf,
	0x57, 0xee, 0x91, 0x11, 0xf7, 0x5b, 0x47, 0x8a, 0x5c, 0x0c, 0x0e, 0xcc, 0x1b, 0xd5, 0xec, 0x24,
	0x3e, 0x5d, 0x86, 0xe9, 0x23, 0xfd, 0xff, 0xff, 0xa1, 0x03, 0xec, 0x27, 0x78, 0x64, 0x53, 0x1c,
	0x36, 0x16, 0x5f, 0x01, 0x99, 0xfe, 0x19, 0x8a, 0x62, 0x12, 0x4a, 0x0e, 0xb7, 0xb5, 0x5c, 0x72,
	0xe5, 0xdb, 0xfb, 0x26, 0xd9, 0xb0, 0x15, 0xad, 0xc8, 0xc4, 0x72, 0x94, 0x3b, 0xbc, 0xe6, 0xfe,
	0xdb, 0x91, 0x78, 0x5d, 0x26, 0x34, 0xe3, 0x28, 0x5b, 0xa2, 0x73, 0xdb, 0x57, 0x0f, 0x2f, 0xeb,
	0xe7, 0x37, 0xe1, 0xfb, 0x19, 0xb6, 0xdf, 0x76, 0x09, 0xc1, 0x9a, 0xac, 0x46, 0xbf, 0xaa, 0xcd,
	0x59, 0x9b, 0xdb, 0xf5, 0x4f, 0x00, 0x00, 0x00, 0xff, 0xff, 0x54, 0x8c, 0xf1, 0xf7, 0x89, 0x02,
	0x00, 0x00,
}
