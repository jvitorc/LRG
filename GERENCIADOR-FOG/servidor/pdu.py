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
    'attribute': ['endereco', 'umidade', 'temperatura', 'gas', 'chamas'],
    'size': [2, 2, 2, 2, 1],
    'payload': ['endereco', 'umidade', 'temperatura', 'gas', 'chamas'],
    'length': 9
}

PDU_TYPE = {
    b'\x11': PDU_INCENDIO,
}
