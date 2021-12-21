with open("16-input.txt") as file:
    line = file.readline().strip()

ini_string = line
scale = 16

res = bin(int(ini_string, scale)).zfill(8)
bits = str(res).strip("0b")


def check_stream(bits: str, timer=0, end: int = len(bits), versionsum=0):
    version = bits[:3]  # unimportant
    type_ID = bits[3:6]  # important if 4 or not
    length_type_ID = bits[6]  # dictates length or number of sub packets
    rest = bits[7:]

    type_ID = int(type_ID, 2)
    version = int(version, 2)
    versionsum += version
    out = ""
    if type_ID == 4:
        for i in range(0, end, 5):
            nibble = rest[i:i+5]
            out += nibble[1:]  # skip indicating number
            if nibble[0] == '0':
                break
        print(out)
        print(int(out, 2))
    else:
        if length_type_ID == '0':  # check next 15 bits
            length_subpackets = rest[:15]
            length_subpackets = int(length_subpackets, 2)
            check_stream(rest[15:], end=length_subpackets,
                         versionsum=versionsum)
        else:  # length_type_ID == '1'
            timer += 1
            length_subpackets = rest[:11]
            length_subpackets = int(length_subpackets, 2)
            if timer <= length_subpackets:
                check_stream(bits=rest[11:], timer=timer,
                             versionsum=versionsum)
    return versionsum


def check(bits, start):
    i = start
    version = bits[:3]  # unimportant
    type_ID = bits[i+3:i+6]  # important if 4 or not
    length_type_ID = bits[6]  # dictates length or number of sub packets
    #rest = bits[7:]

    type_ID = int(type_ID, 2)
    versionsum = int(version, 2)

    i += 6

    if type_ID == 4:
        while True:
            i += 5
            if bits[i-5] == '0':
                break

    else:
        if bits[i] == '0':
            endi = i + 16 + int(bits[i+1:i+16], 2)
            i += 16
            while i < endi:
                i, version = check(bits, i)
                versionsum += version

        else:  # length_type_ID == '1'
            next_packet = int(bits[i+1:i+12], 2)
            i += 12

            for _ in range(next_packet):
                i, version = check(bits, i)
                versionsum += version

    return i, versionsum

def ps1(startbit, bs):
    i = startbit # index into bs
    tv = int(bs[i:i+3],2) # total version
    ID = int(bs[i+3:i+6],2) # packet type ID
    i += 6
    if ID == 4: #literal value
        while True:
            i += 5
            if bs[i-5] == '0': #last value packet
                break
    else:
        if bs[i] == '0':
            endi = i + 16 + int(bs[i+1:i+16],2)
            i += 16
            while i < endi:
                i,v = ps1(i, bs)
                tv += v
        else:
            np = int(bs[i+1:i+12],2)
            i += 12
            for _ in range(np):
                i,v = ps1(i, bs)
                tv += v

    return i,tv

#print("Total of version numbers:",ps1(0, bits)[1])

result = ps1(0, bits)
#result = check(bits, 0)
print(result)
