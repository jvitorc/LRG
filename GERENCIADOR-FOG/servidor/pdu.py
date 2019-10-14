# --------------------------------
#     FUNCTION HANDLES
# --------------------------------


def F_HEX(x):
    return x.hex().upper()


def F_CHAR(x):
    return x.decode('utf-8')

# --------------------------------
#     PDU DESCRIPTION
# --------------------------------

PDU_DEFAULT = {
    'attribute': ['pdu'],
    'size': [1],
    'payload': [],
    'length': 1
}

PDU_INCENDIO = {
    'table': 'INCEDIO',
    'attribute': ['endereco', 'umidade', 'temperatura', 'gas',  'chamas'],
    'format': [F_HEX, F_CHAR, F_CHAR, F_CHAR, F_CHAR],
    'size': [2, 2, 2, 2, 1],
    'payload': ['endereco', 'umidade', 'temperatura', 'gas', 'chamas'],
    'length': 9
}

PDU_RFID = {
    'table': 'RFID',
    'attribute': ['endereco', 'tag'],
    'format': [F_HEX, F_HEX],
    'size': [2, 4],
    'payload': ['endereco', 'tag'],
    'length': 6
}

PDU_TYPE = {
    b'\x11': PDU_INCENDIO,
    b'\x12': PDU_RFID
}
