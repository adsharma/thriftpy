from thriftpy._compat import with_metaclass
from thriftpy.thrift import TPayloadMeta

class FBSType(object):
    BOOL = 0
    BYTE = 1
    UBYTE = 2
    SHORT = 3
    USHORT = 4
    INT = 5
    UINT = 6
    FLOAT = 7
    LONG = 8
    ULONG = 9
    DOUBLE = 10
    STRING = 11
    STRUCT = 12
    TABLE = 13
    UNION = 14
    VECTOR = 15

    _VALUES_TO_NAMES = {
        BOOL :'BOOL',
        BYTE :'BYTE',
        UBYTE :'UBYTE',
        SHORT :'SHORT',
        USHORT :'USHORT',
        INT :'INT',
        UINT :'UINT',
        FLOAT :'FLOAT',
        LONG :'LONG',
        ULONG :'ULONG',
        DOUBLE :'DOUBLE',
        STRING :'STRING',
        STRUCT : 'STRUCT',
        TABLE : 'TABLE',
        UNION : 'UNION'
    }

class FBSPayload(with_metaclass(TPayloadMeta, object)):

    __hash__ = None

    def __repr__(self):
        l = ['%s=%r' % (key, value) for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(l))

    def __str__(self):
        return repr(self)

    def __eq__(self, other):
        return isinstance(other, self.__class__) and \
            self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self.__eq__(other)
