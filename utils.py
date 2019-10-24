def load_zones():

    json_zone = {}
    zone_files = glob.glob('zones/*.zone')

    for zone in zone_files:
        with open(zone) as zone_data:
            data = json.load(zone_data)
            zonename = data["$origin"]
            jsonzone[zonename] = data
    return json_zone

zonedata = load_zones()


def getflags(flags):
    byte1 = bytes(flags[:1])
    byte2 = bytes(flags[1:2])

    rflags = ''

    QR = '1'

    OPCODE = ''
    for bit in range(1,5):
        OPCODE += str(ord(byte1)&(1<<bit))

    AA = '1'

    TC = '0'

    RD = '0'

    # Byte 2

    RA = '0'

    Z = '000'

    RCODE = '0000'

    return int(QR+OPCODE+AA+TC+RD, 2).to_bytes(1, byteorder='big')+int(RA+Z+RCODE, 2).to_bytes(1, byteorder='big')

def getzone(domain):
    global zonedata

    zone_name = '.'.join(domain)
    return zonedata[zone_name]
