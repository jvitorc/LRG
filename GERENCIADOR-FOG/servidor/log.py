from enum import Enum, auto


# --------------------------------
#     LOG TABLE
# --------------------------------
LOG_TABLE_NAME = 'LOG'
LOG_ATTRIBUTES = ['tipo', 'endereco', 'erros', 'data', 'descricao']


# --------------------------------
#     ERROR DESCRIPTION
# --------------------------------
LOG_PACKET_DESCRIPTION_ = """
DEVICE [{}]
REGISTARED (INTERVAL - 1 MIN):
    PACKETS_MIN = {}
    PACKETS_MAX = {}
RECEIVAD (INTERVAL - [{}-{}]):
    PACKETS = {}
"""


# --------------------------------
#
# --------------------------------
class ERRRORS(Enum):
    PACKET_LOSS = auto()
    PACKET_OVERFLOW = auto()
    CONNECTION_LOSS = auto()
    UNREGISTERED_ADDRESS = auto()
