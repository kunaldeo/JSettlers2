# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: data.proto

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
  name='data.proto',
  package='',
  syntax='proto3',
  serialized_pb=_b('\n\ndata.proto\"\x18\n\t_IntArray\x12\x0b\n\x03\x61rr\x18\x01 \x03(\x05\"\x19\n\n_SIntArray\x12\x0b\n\x03\x61rr\x18\x01 \x03(\x11\"\xc2\x01\n\x0bResourceSet\x12\x0c\n\x04\x63lay\x18\x01 \x01(\x05\x12\x0b\n\x03ore\x18\x02 \x01(\x05\x12\r\n\x05sheep\x18\x03 \x01(\x05\x12\r\n\x05wheat\x18\x04 \x01(\x05\x12\x0c\n\x04wood\x18\x05 \x01(\x05\x12*\n\x06others\x18\x06 \x03(\x0b\x32\x1a.ResourceSet.OtherResource\x1a@\n\rOtherResource\x12\x1f\n\x08res_type\x18\x01 \x01(\x0e\x32\r.ResourceType\x12\x0e\n\x06\x61mount\x18\x02 \x01(\x05*a\n\x0cResourceType\x12\x11\n\r_NOT_YET_USED\x10\x00\x12\x08\n\x04\x43LAY\x10\x01\x12\x07\n\x03ORE\x10\x02\x12\t\n\x05SHEEP\x10\x03\x12\t\n\x05WHEAT\x10\x04\x12\x08\n\x04WOOD\x10\x05\x12\x0b\n\x07UNKNOWN\x10\x06*T\n\tPieceType\x12\x08\n\x04ROAD\x10\x00\x12\x0e\n\nSETTLEMENT\x10\x01\x12\x08\n\x04\x43ITY\x10\x02\x12\x08\n\x04SHIP\x10\x03\x12\x0c\n\x08\x46ORTRESS\x10\x04\x12\x0b\n\x07VILLAGE\x10\x05*I\n\x11OtherPlayableItem\x12\x18\n\x14_UNSENT_DEFAULT_ITEM\x10\x00\x12\x0c\n\x08\x44\x45V_CARD\x10\x02\x12\x0c\n\x08INV_ITEM\x10\x03*\xdb\x01\n\x0c\x44\x65vCardValue\x12 \n\x1c_UNSENT_DEFAULT_DEVCARDVALUE\x10\x00\x12\x14\n\x10UNKNOWN_DEV_CARD\x10\x01\x12\n\n\x06KNIGHT\x10\x02\x12\x0c\n\x08MONOPOLY\x10\x03\x12\x11\n\rROAD_BUILDING\x10\x04\x12\x12\n\x0eYEAR_OF_PLENTY\x10\x05\x12\r\n\tVP_CHAPEL\x10\x32\x12\x11\n\rVP_GREAT_HALL\x10\x33\x12\x0e\n\nVP_LIBRARY\x10\x34\x12\r\n\tVP_MARKET\x10\x35\x12\x11\n\rVP_UNIVERSITY\x10\x36*\xa5\x05\n\tGameState\x12\x07\n\x03NEW\x10\x00\x12\t\n\x05READY\x10\x01\x12\"\n\x1eREADY_RESET_WAIT_ROBOT_DISMISS\x10\x04\x12\x0b\n\x07START1A\x10\x05\x12\x0b\n\x07START1B\x10\x06\x12\x0b\n\x07START2A\x10\n\x12)\n%STARTS_WAITING_FOR_PICK_GOLD_RESOURCE\x10\x0e\x12\x0b\n\x07START2B\x10\x0b\x12\x0b\n\x07START3A\x10\x0c\x12\x0b\n\x07START3B\x10\r\x12\x10\n\x0cROLL_OR_CARD\x10\x0f\x12\t\n\x05PLAY1\x10\x14\x12\x10\n\x0cPLACING_ROAD\x10\x1e\x12\x16\n\x12PLACING_SETTLEMENT\x10\x1f\x12\x10\n\x0cPLACING_CITY\x10 \x12\x12\n\x0ePLACING_ROBBER\x10!\x12\x12\n\x0ePLACING_PIRATE\x10\"\x12\x10\n\x0cPLACING_SHIP\x10#\x12\x16\n\x12PLACING_FREE_ROAD1\x10(\x12\x16\n\x12PLACING_FREE_ROAD2\x10)\x12\x14\n\x10PLACING_INV_ITEM\x10*\x12\x18\n\x14WAITING_FOR_DISCARDS\x10\x32\x12!\n\x1dWAITING_FOR_ROB_CHOOSE_PLAYER\x10\x33\x12\x19\n\x15WAITING_FOR_DISCOVERY\x10\x34\x12\x18\n\x14WAITING_FOR_MONOPOLY\x10\x35\x12 \n\x1cWAITING_FOR_ROBBER_OR_PIRATE\x10\x36\x12%\n!WAITING_FOR_ROB_CLOTH_OR_RESOURCE\x10\x37\x12\"\n\x1eWAITING_FOR_PICK_GOLD_RESOURCE\x10\x38\x12\x14\n\x10SPECIAL_BUILDING\x10\x64\x12\t\n\x04OVER\x10\xe8\x07\x12\x0e\n\tRESET_OLD\x10\xe9\x07*=\n\rSeatLockState\x12\x0c\n\x08UNLOCKED\x10\x00\x12\n\n\x06LOCKED\x10\x01\x12\x12\n\x0e\x43LEAR_ON_RESET\x10\x02\x42\r\n\tsoc.protoH\x01\x62\x06proto3')
)

_RESOURCETYPE = _descriptor.EnumDescriptor(
  name='ResourceType',
  full_name='ResourceType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='_NOT_YET_USED', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CLAY', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ORE', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SHEEP', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='WHEAT', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='WOOD', index=5, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=6, number=6,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=264,
  serialized_end=361,
)
_sym_db.RegisterEnumDescriptor(_RESOURCETYPE)

ResourceType = enum_type_wrapper.EnumTypeWrapper(_RESOURCETYPE)
_PIECETYPE = _descriptor.EnumDescriptor(
  name='PieceType',
  full_name='PieceType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ROAD', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SETTLEMENT', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CITY', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SHIP', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FORTRESS', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='VILLAGE', index=5, number=5,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=363,
  serialized_end=447,
)
_sym_db.RegisterEnumDescriptor(_PIECETYPE)

PieceType = enum_type_wrapper.EnumTypeWrapper(_PIECETYPE)
_OTHERPLAYABLEITEM = _descriptor.EnumDescriptor(
  name='OtherPlayableItem',
  full_name='OtherPlayableItem',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='_UNSENT_DEFAULT_ITEM', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DEV_CARD', index=1, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INV_ITEM', index=2, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=449,
  serialized_end=522,
)
_sym_db.RegisterEnumDescriptor(_OTHERPLAYABLEITEM)

OtherPlayableItem = enum_type_wrapper.EnumTypeWrapper(_OTHERPLAYABLEITEM)
_DEVCARDVALUE = _descriptor.EnumDescriptor(
  name='DevCardValue',
  full_name='DevCardValue',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='_UNSENT_DEFAULT_DEVCARDVALUE', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN_DEV_CARD', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='KNIGHT', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MONOPOLY', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ROAD_BUILDING', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='YEAR_OF_PLENTY', index=5, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='VP_CHAPEL', index=6, number=50,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='VP_GREAT_HALL', index=7, number=51,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='VP_LIBRARY', index=8, number=52,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='VP_MARKET', index=9, number=53,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='VP_UNIVERSITY', index=10, number=54,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=525,
  serialized_end=744,
)
_sym_db.RegisterEnumDescriptor(_DEVCARDVALUE)

DevCardValue = enum_type_wrapper.EnumTypeWrapper(_DEVCARDVALUE)
_GAMESTATE = _descriptor.EnumDescriptor(
  name='GameState',
  full_name='GameState',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NEW', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='READY', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='READY_RESET_WAIT_ROBOT_DISMISS', index=2, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='START1A', index=3, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='START1B', index=4, number=6,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='START2A', index=5, number=10,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STARTS_WAITING_FOR_PICK_GOLD_RESOURCE', index=6, number=14,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='START2B', index=7, number=11,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='START3A', index=8, number=12,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='START3B', index=9, number=13,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ROLL_OR_CARD', index=10, number=15,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PLAY1', index=11, number=20,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PLACING_ROAD', index=12, number=30,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PLACING_SETTLEMENT', index=13, number=31,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PLACING_CITY', index=14, number=32,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PLACING_ROBBER', index=15, number=33,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PLACING_PIRATE', index=16, number=34,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PLACING_SHIP', index=17, number=35,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PLACING_FREE_ROAD1', index=18, number=40,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PLACING_FREE_ROAD2', index=19, number=41,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PLACING_INV_ITEM', index=20, number=42,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='WAITING_FOR_DISCARDS', index=21, number=50,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='WAITING_FOR_ROB_CHOOSE_PLAYER', index=22, number=51,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='WAITING_FOR_DISCOVERY', index=23, number=52,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='WAITING_FOR_MONOPOLY', index=24, number=53,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='WAITING_FOR_ROBBER_OR_PIRATE', index=25, number=54,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='WAITING_FOR_ROB_CLOTH_OR_RESOURCE', index=26, number=55,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='WAITING_FOR_PICK_GOLD_RESOURCE', index=27, number=56,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SPECIAL_BUILDING', index=28, number=100,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OVER', index=29, number=1000,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RESET_OLD', index=30, number=1001,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=747,
  serialized_end=1424,
)
_sym_db.RegisterEnumDescriptor(_GAMESTATE)

GameState = enum_type_wrapper.EnumTypeWrapper(_GAMESTATE)
_SEATLOCKSTATE = _descriptor.EnumDescriptor(
  name='SeatLockState',
  full_name='SeatLockState',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNLOCKED', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LOCKED', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CLEAR_ON_RESET', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1426,
  serialized_end=1487,
)
_sym_db.RegisterEnumDescriptor(_SEATLOCKSTATE)

SeatLockState = enum_type_wrapper.EnumTypeWrapper(_SEATLOCKSTATE)
_NOT_YET_USED = 0
CLAY = 1
ORE = 2
SHEEP = 3
WHEAT = 4
WOOD = 5
UNKNOWN = 6
ROAD = 0
SETTLEMENT = 1
CITY = 2
SHIP = 3
FORTRESS = 4
VILLAGE = 5
_UNSENT_DEFAULT_ITEM = 0
DEV_CARD = 2
INV_ITEM = 3
_UNSENT_DEFAULT_DEVCARDVALUE = 0
UNKNOWN_DEV_CARD = 1
KNIGHT = 2
MONOPOLY = 3
ROAD_BUILDING = 4
YEAR_OF_PLENTY = 5
VP_CHAPEL = 50
VP_GREAT_HALL = 51
VP_LIBRARY = 52
VP_MARKET = 53
VP_UNIVERSITY = 54
NEW = 0
READY = 1
READY_RESET_WAIT_ROBOT_DISMISS = 4
START1A = 5
START1B = 6
START2A = 10
STARTS_WAITING_FOR_PICK_GOLD_RESOURCE = 14
START2B = 11
START3A = 12
START3B = 13
ROLL_OR_CARD = 15
PLAY1 = 20
PLACING_ROAD = 30
PLACING_SETTLEMENT = 31
PLACING_CITY = 32
PLACING_ROBBER = 33
PLACING_PIRATE = 34
PLACING_SHIP = 35
PLACING_FREE_ROAD1 = 40
PLACING_FREE_ROAD2 = 41
PLACING_INV_ITEM = 42
WAITING_FOR_DISCARDS = 50
WAITING_FOR_ROB_CHOOSE_PLAYER = 51
WAITING_FOR_DISCOVERY = 52
WAITING_FOR_MONOPOLY = 53
WAITING_FOR_ROBBER_OR_PIRATE = 54
WAITING_FOR_ROB_CLOTH_OR_RESOURCE = 55
WAITING_FOR_PICK_GOLD_RESOURCE = 56
SPECIAL_BUILDING = 100
OVER = 1000
RESET_OLD = 1001
UNLOCKED = 0
LOCKED = 1
CLEAR_ON_RESET = 2



__INTARRAY = _descriptor.Descriptor(
  name='_IntArray',
  full_name='_IntArray',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='arr', full_name='_IntArray.arr', index=0,
      number=1, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
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
  ],
  serialized_start=14,
  serialized_end=38,
)


__SINTARRAY = _descriptor.Descriptor(
  name='_SIntArray',
  full_name='_SIntArray',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='arr', full_name='_SIntArray.arr', index=0,
      number=1, type=17, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
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
  ],
  serialized_start=40,
  serialized_end=65,
)


_RESOURCESET_OTHERRESOURCE = _descriptor.Descriptor(
  name='OtherResource',
  full_name='ResourceSet.OtherResource',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='res_type', full_name='ResourceSet.OtherResource.res_type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='amount', full_name='ResourceSet.OtherResource.amount', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  ],
  serialized_start=198,
  serialized_end=262,
)

_RESOURCESET = _descriptor.Descriptor(
  name='ResourceSet',
  full_name='ResourceSet',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='clay', full_name='ResourceSet.clay', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ore', full_name='ResourceSet.ore', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sheep', full_name='ResourceSet.sheep', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='wheat', full_name='ResourceSet.wheat', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='wood', full_name='ResourceSet.wood', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='others', full_name='ResourceSet.others', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_RESOURCESET_OTHERRESOURCE, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=68,
  serialized_end=262,
)

_RESOURCESET_OTHERRESOURCE.fields_by_name['res_type'].enum_type = _RESOURCETYPE
_RESOURCESET_OTHERRESOURCE.containing_type = _RESOURCESET
_RESOURCESET.fields_by_name['others'].message_type = _RESOURCESET_OTHERRESOURCE
DESCRIPTOR.message_types_by_name['_IntArray'] = __INTARRAY
DESCRIPTOR.message_types_by_name['_SIntArray'] = __SINTARRAY
DESCRIPTOR.message_types_by_name['ResourceSet'] = _RESOURCESET
DESCRIPTOR.enum_types_by_name['ResourceType'] = _RESOURCETYPE
DESCRIPTOR.enum_types_by_name['PieceType'] = _PIECETYPE
DESCRIPTOR.enum_types_by_name['OtherPlayableItem'] = _OTHERPLAYABLEITEM
DESCRIPTOR.enum_types_by_name['DevCardValue'] = _DEVCARDVALUE
DESCRIPTOR.enum_types_by_name['GameState'] = _GAMESTATE
DESCRIPTOR.enum_types_by_name['SeatLockState'] = _SEATLOCKSTATE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

_IntArray = _reflection.GeneratedProtocolMessageType('_IntArray', (_message.Message,), dict(
  DESCRIPTOR = __INTARRAY,
  __module__ = 'data_pb2'
  # @@protoc_insertion_point(class_scope:_IntArray)
  ))
_sym_db.RegisterMessage(_IntArray)

_SIntArray = _reflection.GeneratedProtocolMessageType('_SIntArray', (_message.Message,), dict(
  DESCRIPTOR = __SINTARRAY,
  __module__ = 'data_pb2'
  # @@protoc_insertion_point(class_scope:_SIntArray)
  ))
_sym_db.RegisterMessage(_SIntArray)

ResourceSet = _reflection.GeneratedProtocolMessageType('ResourceSet', (_message.Message,), dict(

  OtherResource = _reflection.GeneratedProtocolMessageType('OtherResource', (_message.Message,), dict(
    DESCRIPTOR = _RESOURCESET_OTHERRESOURCE,
    __module__ = 'data_pb2'
    # @@protoc_insertion_point(class_scope:ResourceSet.OtherResource)
    ))
  ,
  DESCRIPTOR = _RESOURCESET,
  __module__ = 'data_pb2'
  # @@protoc_insertion_point(class_scope:ResourceSet)
  ))
_sym_db.RegisterMessage(ResourceSet)
_sym_db.RegisterMessage(ResourceSet.OtherResource)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\tsoc.protoH\001'))
# @@protoc_insertion_point(module_scope)
