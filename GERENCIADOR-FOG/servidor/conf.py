# --------------------------------
#     SERVER COFIGURATION
# --------------------------------
FOG_SERVER_START = True
FOG_SERVER_HOST = '192.168.50.166'
FOG_SERVER_PORT = 8081
WEB_SERVER_HOST = ''
WEB_SERVER_PORT = ''

# --------------------------------
#     SERIAL PORT COFIGURATION
# --------------------------------
SERIAL_READ = True
SERIAL_PORT = '/dev/ttyACM0'
SERIAL_BAUDRATE = 115200

# --------------------------------
#     DATABASE COFIGURATION
# --------------------------------
DB_HOST = 'localhost'
DB_NAME = 'lrg'
DB_USER = 'joaov'
DB_PASSWORD = '1234'

# --------------------------------
#     DEVICE CONTROL
# --------------------------------
D_MIN = 0
D_MAX = 1

DEVICES = {
    'AAA4': (0, 2),
    'AAA8': (10, 14)
}
