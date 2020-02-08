# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: movie.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='movie.proto',
  package='movie',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x0bmovie.proto\x12\x05movie\"\xea\x01\n\x05Movie\x12\n\n\x02id\x18\x01 \x01(\t\x12\r\n\x05title\x18\x02 \x01(\t\x12!\n\x06genres\x18\x03 \x03(\x0e\x32\x11.movie.MovieGenre\x12%\n\tdirectors\x18\x04 \x03(\x0b\x32\x12.movie.MoviePerson\x12#\n\x07writers\x18\x05 \x03(\x0b\x32\x12.movie.MoviePerson\x12!\n\x05stars\x18\x06 \x03(\x0b\x32\x12.movie.MoviePerson\x12\x1a\n\x12year_of_production\x18\x07 \x01(\x05\x12\x18\n\x10\x64uration_minutes\x18\x08 \x01(\x05\"4\n\x0bMoviePerson\x12\x12\n\nfirst_name\x18\x01 \x01(\t\x12\x11\n\tlast_name\x18\x02 \x01(\t\"$\n\x10\x41\x64\x64MovieResponse\x12\x10\n\x08movie_id\x18\x01 \x01(\t*k\n\nMovieGenre\x12\n\n\x06\x41\x43TION\x10\x00\x12\n\n\x06\x43OMEDY\x10\x01\x12\t\n\x05\x44RAMA\x10\x02\x12\n\n\x06HORROR\x10\x03\x12\n\n\x06SCI_FI\x10\x04\x12\x0c\n\x08THRILLER\x10\x05\x12\x07\n\x03WAR\x10\x06\x12\x0b\n\x07WESTERN\x10\x07\x32\x43\n\x0cMovieService\x12\x33\n\x08\x41\x64\x64Movie\x12\x0c.movie.Movie\x1a\x17.movie.AddMovieResponse\"\x00\x62\x06proto3')
)

_MOVIEGENRE = _descriptor.EnumDescriptor(
  name='MovieGenre',
  full_name='movie.MovieGenre',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ACTION', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COMEDY', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DRAMA', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='HORROR', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SCI_FI', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='THRILLER', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='WAR', index=6, number=6,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='WESTERN', index=7, number=7,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=351,
  serialized_end=458,
)
_sym_db.RegisterEnumDescriptor(_MOVIEGENRE)

MovieGenre = enum_type_wrapper.EnumTypeWrapper(_MOVIEGENRE)
ACTION = 0
COMEDY = 1
DRAMA = 2
HORROR = 3
SCI_FI = 4
THRILLER = 5
WAR = 6
WESTERN = 7



_MOVIE = _descriptor.Descriptor(
  name='Movie',
  full_name='movie.Movie',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='movie.Movie.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='title', full_name='movie.Movie.title', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='genres', full_name='movie.Movie.genres', index=2,
      number=3, type=14, cpp_type=8, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='directors', full_name='movie.Movie.directors', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='writers', full_name='movie.Movie.writers', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='stars', full_name='movie.Movie.stars', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='year_of_production', full_name='movie.Movie.year_of_production', index=6,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='duration_minutes', full_name='movie.Movie.duration_minutes', index=7,
      number=8, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=23,
  serialized_end=257,
)


_MOVIEPERSON = _descriptor.Descriptor(
  name='MoviePerson',
  full_name='movie.MoviePerson',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='first_name', full_name='movie.MoviePerson.first_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='last_name', full_name='movie.MoviePerson.last_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=259,
  serialized_end=311,
)


_ADDMOVIERESPONSE = _descriptor.Descriptor(
  name='AddMovieResponse',
  full_name='movie.AddMovieResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='movie_id', full_name='movie.AddMovieResponse.movie_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=313,
  serialized_end=349,
)

_MOVIE.fields_by_name['genres'].enum_type = _MOVIEGENRE
_MOVIE.fields_by_name['directors'].message_type = _MOVIEPERSON
_MOVIE.fields_by_name['writers'].message_type = _MOVIEPERSON
_MOVIE.fields_by_name['stars'].message_type = _MOVIEPERSON
DESCRIPTOR.message_types_by_name['Movie'] = _MOVIE
DESCRIPTOR.message_types_by_name['MoviePerson'] = _MOVIEPERSON
DESCRIPTOR.message_types_by_name['AddMovieResponse'] = _ADDMOVIERESPONSE
DESCRIPTOR.enum_types_by_name['MovieGenre'] = _MOVIEGENRE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Movie = _reflection.GeneratedProtocolMessageType('Movie', (_message.Message,), {
  'DESCRIPTOR' : _MOVIE,
  '__module__' : 'movie_pb2'
  # @@protoc_insertion_point(class_scope:movie.Movie)
  })
_sym_db.RegisterMessage(Movie)

MoviePerson = _reflection.GeneratedProtocolMessageType('MoviePerson', (_message.Message,), {
  'DESCRIPTOR' : _MOVIEPERSON,
  '__module__' : 'movie_pb2'
  # @@protoc_insertion_point(class_scope:movie.MoviePerson)
  })
_sym_db.RegisterMessage(MoviePerson)

AddMovieResponse = _reflection.GeneratedProtocolMessageType('AddMovieResponse', (_message.Message,), {
  'DESCRIPTOR' : _ADDMOVIERESPONSE,
  '__module__' : 'movie_pb2'
  # @@protoc_insertion_point(class_scope:movie.AddMovieResponse)
  })
_sym_db.RegisterMessage(AddMovieResponse)



_MOVIESERVICE = _descriptor.ServiceDescriptor(
  name='MovieService',
  full_name='movie.MovieService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=460,
  serialized_end=527,
  methods=[
  _descriptor.MethodDescriptor(
    name='AddMovie',
    full_name='movie.MovieService.AddMovie',
    index=0,
    containing_service=None,
    input_type=_MOVIE,
    output_type=_ADDMOVIERESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_MOVIESERVICE)

DESCRIPTOR.services_by_name['MovieService'] = _MOVIESERVICE

# @@protoc_insertion_point(module_scope)