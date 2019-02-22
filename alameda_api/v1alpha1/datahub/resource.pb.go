// Code generated by protoc-gen-go. DO NOT EDIT.
// source: alameda_api/v1alpha1/datahub/resource.proto

package containers_ai_alameda_v1alpha1_datahub

import proto "github.com/golang/protobuf/proto"
import fmt "fmt"
import math "math"
import timestamp "github.com/golang/protobuf/ptypes/timestamp"

// Reference imports to suppress errors if they are not otherwise used.
var _ = proto.Marshal
var _ = fmt.Errorf
var _ = math.Inf

// This is a compile-time assertion to ensure that this generated file
// is compatible with the proto package it is being compiled against.
// A compilation error at this line likely means your copy of the
// proto package needs to be updated.
const _ = proto.ProtoPackageIsVersion2 // please upgrade the proto package

// *
// Represents kubernetes resource kind
//
type Kind int32

const (
	Kind_POD              Kind = 0
	Kind_DEPLOYMENT       Kind = 1
	Kind_DEPLOYMENTCONFIG Kind = 2
)

var Kind_name = map[int32]string{
	0: "POD",
	1: "DEPLOYMENT",
	2: "DEPLOYMENTCONFIG",
}
var Kind_value = map[string]int32{
	"POD":              0,
	"DEPLOYMENT":       1,
	"DEPLOYMENTCONFIG": 2,
}

func (x Kind) String() string {
	return proto.EnumName(Kind_name, int32(x))
}
func (Kind) EnumDescriptor() ([]byte, []int) {
	return fileDescriptor_resource_2774a3a8585b3290, []int{0}
}

// *
// Represents a container and its containing limit and requeset configurations
//
type Container struct {
	Name                 string        `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
	LimitResource        []*MetricData `protobuf:"bytes,2,rep,name=limit_resource,json=limitResource,proto3" json:"limit_resource,omitempty"`
	RequestResource      []*MetricData `protobuf:"bytes,3,rep,name=request_resource,json=requestResource,proto3" json:"request_resource,omitempty"`
	XXX_NoUnkeyedLiteral struct{}      `json:"-"`
	XXX_unrecognized     []byte        `json:"-"`
	XXX_sizecache        int32         `json:"-"`
}

func (m *Container) Reset()         { *m = Container{} }
func (m *Container) String() string { return proto.CompactTextString(m) }
func (*Container) ProtoMessage()    {}
func (*Container) Descriptor() ([]byte, []int) {
	return fileDescriptor_resource_2774a3a8585b3290, []int{0}
}
func (m *Container) XXX_Unmarshal(b []byte) error {
	return xxx_messageInfo_Container.Unmarshal(m, b)
}
func (m *Container) XXX_Marshal(b []byte, deterministic bool) ([]byte, error) {
	return xxx_messageInfo_Container.Marshal(b, m, deterministic)
}
func (dst *Container) XXX_Merge(src proto.Message) {
	xxx_messageInfo_Container.Merge(dst, src)
}
func (m *Container) XXX_Size() int {
	return xxx_messageInfo_Container.Size(m)
}
func (m *Container) XXX_DiscardUnknown() {
	xxx_messageInfo_Container.DiscardUnknown(m)
}

var xxx_messageInfo_Container proto.InternalMessageInfo

func (m *Container) GetName() string {
	if m != nil {
		return m.Name
	}
	return ""
}

func (m *Container) GetLimitResource() []*MetricData {
	if m != nil {
		return m.LimitResource
	}
	return nil
}

func (m *Container) GetRequestResource() []*MetricData {
	if m != nil {
		return m.RequestResource
	}
	return nil
}

// *
// Represents a Kubernetes pod
//
type Pod struct {
	NamespacedName       *NamespacedName      `protobuf:"bytes,1,opt,name=namespaced_name,json=namespacedName,proto3" json:"namespaced_name,omitempty"`
	ResourceLink         string               `protobuf:"bytes,2,opt,name=resource_link,json=resourceLink,proto3" json:"resource_link,omitempty"`
	Containers           []*Container         `protobuf:"bytes,3,rep,name=containers,proto3" json:"containers,omitempty"`
	IsAlameda            bool                 `protobuf:"varint,4,opt,name=is_alameda,json=isAlameda,proto3" json:"is_alameda,omitempty"`
	AlamedaScaler        *NamespacedName      `protobuf:"bytes,5,opt,name=alameda_scaler,json=alamedaScaler,proto3" json:"alameda_scaler,omitempty"`
	NodeName             string               `protobuf:"bytes,6,opt,name=node_name,json=nodeName,proto3" json:"node_name,omitempty"`
	StartTime            *timestamp.Timestamp `protobuf:"bytes,7,opt,name=start_time,json=startTime,proto3" json:"start_time,omitempty"`
	Policy               RecommendationPolicy `protobuf:"varint,8,opt,name=policy,proto3,enum=containers_ai.alameda.v1alpha1.datahub.RecommendationPolicy" json:"policy,omitempty"`
	XXX_NoUnkeyedLiteral struct{}             `json:"-"`
	XXX_unrecognized     []byte               `json:"-"`
	XXX_sizecache        int32                `json:"-"`
}

func (m *Pod) Reset()         { *m = Pod{} }
func (m *Pod) String() string { return proto.CompactTextString(m) }
func (*Pod) ProtoMessage()    {}
func (*Pod) Descriptor() ([]byte, []int) {
	return fileDescriptor_resource_2774a3a8585b3290, []int{1}
}
func (m *Pod) XXX_Unmarshal(b []byte) error {
	return xxx_messageInfo_Pod.Unmarshal(m, b)
}
func (m *Pod) XXX_Marshal(b []byte, deterministic bool) ([]byte, error) {
	return xxx_messageInfo_Pod.Marshal(b, m, deterministic)
}
func (dst *Pod) XXX_Merge(src proto.Message) {
	xxx_messageInfo_Pod.Merge(dst, src)
}
func (m *Pod) XXX_Size() int {
	return xxx_messageInfo_Pod.Size(m)
}
func (m *Pod) XXX_DiscardUnknown() {
	xxx_messageInfo_Pod.DiscardUnknown(m)
}

var xxx_messageInfo_Pod proto.InternalMessageInfo

func (m *Pod) GetNamespacedName() *NamespacedName {
	if m != nil {
		return m.NamespacedName
	}
	return nil
}

func (m *Pod) GetResourceLink() string {
	if m != nil {
		return m.ResourceLink
	}
	return ""
}

func (m *Pod) GetContainers() []*Container {
	if m != nil {
		return m.Containers
	}
	return nil
}

func (m *Pod) GetIsAlameda() bool {
	if m != nil {
		return m.IsAlameda
	}
	return false
}

func (m *Pod) GetAlamedaScaler() *NamespacedName {
	if m != nil {
		return m.AlamedaScaler
	}
	return nil
}

func (m *Pod) GetNodeName() string {
	if m != nil {
		return m.NodeName
	}
	return ""
}

func (m *Pod) GetStartTime() *timestamp.Timestamp {
	if m != nil {
		return m.StartTime
	}
	return nil
}

func (m *Pod) GetPolicy() RecommendationPolicy {
	if m != nil {
		return m.Policy
	}
	return RecommendationPolicy_RECOMMENDATIONPOLICY_UNDEFINED
}

// *
// Represents the capacity of a Kubernetes node
//
type Capacity struct {
	CpuCores                 int64    `protobuf:"varint,1,opt,name=cpu_cores,json=cpuCores,proto3" json:"cpu_cores,omitempty"`
	MemoryBytes              int64    `protobuf:"varint,2,opt,name=memory_bytes,json=memoryBytes,proto3" json:"memory_bytes,omitempty"`
	NetwotkMegabitsPerSecond int64    `protobuf:"varint,3,opt,name=netwotk_megabits_per_second,json=netwotkMegabitsPerSecond,proto3" json:"netwotk_megabits_per_second,omitempty"`
	XXX_NoUnkeyedLiteral     struct{} `json:"-"`
	XXX_unrecognized         []byte   `json:"-"`
	XXX_sizecache            int32    `json:"-"`
}

func (m *Capacity) Reset()         { *m = Capacity{} }
func (m *Capacity) String() string { return proto.CompactTextString(m) }
func (*Capacity) ProtoMessage()    {}
func (*Capacity) Descriptor() ([]byte, []int) {
	return fileDescriptor_resource_2774a3a8585b3290, []int{2}
}
func (m *Capacity) XXX_Unmarshal(b []byte) error {
	return xxx_messageInfo_Capacity.Unmarshal(m, b)
}
func (m *Capacity) XXX_Marshal(b []byte, deterministic bool) ([]byte, error) {
	return xxx_messageInfo_Capacity.Marshal(b, m, deterministic)
}
func (dst *Capacity) XXX_Merge(src proto.Message) {
	xxx_messageInfo_Capacity.Merge(dst, src)
}
func (m *Capacity) XXX_Size() int {
	return xxx_messageInfo_Capacity.Size(m)
}
func (m *Capacity) XXX_DiscardUnknown() {
	xxx_messageInfo_Capacity.DiscardUnknown(m)
}

var xxx_messageInfo_Capacity proto.InternalMessageInfo

func (m *Capacity) GetCpuCores() int64 {
	if m != nil {
		return m.CpuCores
	}
	return 0
}

func (m *Capacity) GetMemoryBytes() int64 {
	if m != nil {
		return m.MemoryBytes
	}
	return 0
}

func (m *Capacity) GetNetwotkMegabitsPerSecond() int64 {
	if m != nil {
		return m.NetwotkMegabitsPerSecond
	}
	return 0
}

// *
// Represents a Kubernetes node
//
type Node struct {
	Name                 string    `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
	Capacity             *Capacity `protobuf:"bytes,2,opt,name=capacity,proto3" json:"capacity,omitempty"`
	XXX_NoUnkeyedLiteral struct{}  `json:"-"`
	XXX_unrecognized     []byte    `json:"-"`
	XXX_sizecache        int32     `json:"-"`
}

func (m *Node) Reset()         { *m = Node{} }
func (m *Node) String() string { return proto.CompactTextString(m) }
func (*Node) ProtoMessage()    {}
func (*Node) Descriptor() ([]byte, []int) {
	return fileDescriptor_resource_2774a3a8585b3290, []int{3}
}
func (m *Node) XXX_Unmarshal(b []byte) error {
	return xxx_messageInfo_Node.Unmarshal(m, b)
}
func (m *Node) XXX_Marshal(b []byte, deterministic bool) ([]byte, error) {
	return xxx_messageInfo_Node.Marshal(b, m, deterministic)
}
func (dst *Node) XXX_Merge(src proto.Message) {
	xxx_messageInfo_Node.Merge(dst, src)
}
func (m *Node) XXX_Size() int {
	return xxx_messageInfo_Node.Size(m)
}
func (m *Node) XXX_DiscardUnknown() {
	xxx_messageInfo_Node.DiscardUnknown(m)
}

var xxx_messageInfo_Node proto.InternalMessageInfo

func (m *Node) GetName() string {
	if m != nil {
		return m.Name
	}
	return ""
}

func (m *Node) GetCapacity() *Capacity {
	if m != nil {
		return m.Capacity
	}
	return nil
}

func init() {
	proto.RegisterType((*Container)(nil), "containers_ai.alameda.v1alpha1.datahub.Container")
	proto.RegisterType((*Pod)(nil), "containers_ai.alameda.v1alpha1.datahub.Pod")
	proto.RegisterType((*Capacity)(nil), "containers_ai.alameda.v1alpha1.datahub.Capacity")
	proto.RegisterType((*Node)(nil), "containers_ai.alameda.v1alpha1.datahub.Node")
	proto.RegisterEnum("containers_ai.alameda.v1alpha1.datahub.Kind", Kind_name, Kind_value)
}

func init() {
	proto.RegisterFile("alameda_api/v1alpha1/datahub/resource.proto", fileDescriptor_resource_2774a3a8585b3290)
}

var fileDescriptor_resource_2774a3a8585b3290 = []byte{
	// 584 bytes of a gzipped FileDescriptorProto
	0x1f, 0x8b, 0x08, 0x00, 0x00, 0x00, 0x00, 0x00, 0x02, 0xff, 0xa4, 0x53, 0x5f, 0x6b, 0x13, 0x4f,
	0x14, 0xfd, 0x6d, 0x37, 0xbf, 0x36, 0xb9, 0x69, 0xd3, 0x30, 0xf8, 0xb0, 0xb4, 0x88, 0x31, 0x82,
	0xc4, 0x0a, 0x1b, 0x1b, 0x51, 0x10, 0xf4, 0x41, 0xd3, 0x2a, 0x62, 0x9b, 0xc6, 0x6d, 0x5f, 0xfa,
	0x50, 0x86, 0xc9, 0xec, 0xb5, 0x1d, 0xb2, 0x3b, 0xb3, 0xce, 0x4c, 0x94, 0x7c, 0x04, 0xfd, 0x86,
	0x7e, 0x1b, 0xd9, 0xc9, 0x6c, 0x5a, 0x41, 0x6a, 0xd0, 0xb7, 0xb9, 0x77, 0xcf, 0x39, 0xf7, 0xdf,
	0x59, 0x78, 0xcc, 0x32, 0x96, 0x63, 0xca, 0x28, 0x2b, 0x44, 0xff, 0xcb, 0x3e, 0xcb, 0x8a, 0x2b,
	0xb6, 0xdf, 0x4f, 0x99, 0x65, 0x57, 0xb3, 0x49, 0x5f, 0xa3, 0x51, 0x33, 0xcd, 0x31, 0x2e, 0xb4,
	0xb2, 0x8a, 0x3c, 0xe4, 0x4a, 0x5a, 0x26, 0x24, 0x6a, 0x43, 0x99, 0x88, 0x3d, 0x35, 0xae, 0x68,
	0xb1, 0xa7, 0xed, 0xec, 0xdd, 0x2a, 0x5a, 0x68, 0x4c, 0x05, 0xb7, 0x0b, 0xcd, 0x9d, 0x7b, 0x97,
	0x4a, 0x5d, 0x66, 0xd8, 0x77, 0xd1, 0x64, 0xf6, 0xa9, 0x6f, 0x45, 0x8e, 0xc6, 0xb2, 0xbc, 0xf0,
	0x80, 0xdb, 0x3b, 0xcc, 0xd1, 0xb2, 0xf2, 0xed, 0xc1, 0x8f, 0xfe, 0x04, 0xd6, 0x82, 0x2f, 0xa0,
	0xdd, 0x1f, 0x01, 0x34, 0x86, 0xd5, 0x3c, 0x84, 0x40, 0x4d, 0xb2, 0x1c, 0xa3, 0xa0, 0x13, 0xf4,
	0x1a, 0x89, 0x7b, 0x93, 0x73, 0x68, 0x65, 0x22, 0x17, 0x96, 0x56, 0x6b, 0x88, 0xd6, 0x3a, 0x61,
	0xaf, 0x39, 0x18, 0xc4, 0xab, 0xed, 0x21, 0x3e, 0x76, 0xf5, 0x0e, 0x98, 0x65, 0xc9, 0x96, 0x53,
	0x4a, 0xbc, 0x10, 0xb9, 0x80, 0xb6, 0xc6, 0xcf, 0x33, 0x34, 0x37, 0xc4, 0xc3, 0xbf, 0x16, 0xdf,
	0xf6, 0x5a, 0x95, 0x7c, 0xf7, 0x7b, 0x0d, 0xc2, 0xb1, 0x4a, 0x09, 0x85, 0xed, 0x72, 0x12, 0x53,
	0x30, 0x8e, 0x29, 0x5d, 0x0e, 0xd8, 0x1c, 0x3c, 0x5f, 0xb5, 0xca, 0x68, 0x49, 0x2f, 0x5f, 0x49,
	0x4b, 0xfe, 0x12, 0x93, 0x07, 0xb0, 0x55, 0xf5, 0x4f, 0x33, 0x21, 0xa7, 0xd1, 0x9a, 0xdb, 0xdf,
	0x66, 0x95, 0x3c, 0x12, 0x72, 0x4a, 0x3e, 0x02, 0x5c, 0x57, 0xf3, 0x63, 0xee, 0xaf, 0xda, 0xc0,
	0xf2, 0x44, 0xc9, 0x0d, 0x11, 0x72, 0x17, 0x40, 0x18, 0xea, 0x49, 0x51, 0xad, 0x13, 0xf4, 0xea,
	0x49, 0x43, 0x98, 0xd7, 0x8b, 0x04, 0xb9, 0x80, 0x56, 0x65, 0x04, 0xc3, 0x59, 0x86, 0x3a, 0xfa,
	0xff, 0x9f, 0xc6, 0xde, 0xf2, 0xc0, 0x53, 0x27, 0x46, 0x76, 0xa1, 0x21, 0x55, 0x8a, 0x8b, 0x85,
	0xae, 0xbb, 0x89, 0xeb, 0x65, 0xc2, 0xad, 0xe4, 0x05, 0x80, 0xb1, 0x4c, 0x5b, 0x5a, 0x1a, 0x39,
	0xda, 0x70, 0x75, 0x77, 0xe2, 0x85, 0xcb, 0xe3, 0xca, 0xe5, 0xf1, 0x59, 0xe5, 0xf2, 0xa4, 0xe1,
	0xd0, 0x65, 0x4c, 0xce, 0x60, 0xbd, 0x50, 0x99, 0xe0, 0xf3, 0xa8, 0xde, 0x09, 0x7a, 0xad, 0xc1,
	0xcb, 0x55, 0xdb, 0x4d, 0x90, 0xab, 0x3c, 0x47, 0x99, 0x32, 0x2b, 0x94, 0x1c, 0x3b, 0x8d, 0xc4,
	0x6b, 0x75, 0xbf, 0x05, 0x50, 0x1f, 0xb2, 0x82, 0x71, 0x61, 0xe7, 0x65, 0xeb, 0xbc, 0x98, 0x51,
	0xae, 0x34, 0x1a, 0xe7, 0x85, 0x30, 0xa9, 0xf3, 0x62, 0x36, 0x2c, 0x63, 0x72, 0x1f, 0x36, 0x73,
	0xcc, 0x95, 0x9e, 0xd3, 0xc9, 0xdc, 0xa2, 0x71, 0xc7, 0x0c, 0x93, 0xe6, 0x22, 0xf7, 0xa6, 0x4c,
	0x91, 0x57, 0xb0, 0x2b, 0xd1, 0x7e, 0x55, 0x76, 0x4a, 0x73, 0xbc, 0x64, 0x13, 0x61, 0x0d, 0x2d,
	0x50, 0x53, 0x83, 0x5c, 0xc9, 0x34, 0x0a, 0x1d, 0x23, 0xf2, 0x90, 0x63, 0x8f, 0x18, 0xa3, 0x3e,
	0x75, 0xdf, 0xbb, 0x57, 0x50, 0x1b, 0xa9, 0x14, 0x7f, 0xfb, 0xbb, 0x1d, 0x41, 0x9d, 0xfb, 0x36,
	0x5d, 0xe5, 0xe6, 0xe0, 0xc9, 0xca, 0x26, 0xf1, 0xbc, 0x64, 0xa9, 0xb0, 0xf7, 0x0c, 0x6a, 0x1f,
	0x84, 0x4c, 0xc9, 0x06, 0x84, 0xe3, 0x93, 0x83, 0xf6, 0x7f, 0xa4, 0x05, 0x70, 0x70, 0x38, 0x3e,
	0x3a, 0x39, 0x3f, 0x3e, 0x1c, 0x9d, 0xb5, 0x03, 0x72, 0x07, 0xda, 0xd7, 0xf1, 0xf0, 0x64, 0xf4,
	0xf6, 0xfd, 0xbb, 0xf6, 0xda, 0x64, 0xdd, 0x5d, 0xe8, 0xe9, 0xcf, 0x00, 0x00, 0x00, 0xff, 0xff,
	0xd1, 0x36, 0xc2, 0x1d, 0x18, 0x05, 0x00, 0x00,
}
