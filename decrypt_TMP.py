import sys
import re

if len(sys.argv) < 3:
    print("ERR: please inform the TMP file and the output file.")
    sys.exit(1)

input_file = open(sys.argv[1], 'r')
output_file = sys.argv[2]

buff = []
key_code = []

while (True):
    line = input_file.readline()

    if not line:
        break

    rgx_buff = re.match("byte\[\] buff = new byte\[\] {(.*)}", line)

    if (rgx_buff):
        buff = rgx_buff.group(1).split(',')


    rgx_key = re.match("byte\[\] key_code = new byte\[\] {(.*)}", line)

    if (rgx_key):
        key_code = rgx_key.group(1).split(',')


decrypted = []
j = 0
for i in range(len(buff)):
    decrypted.append(int(buff[i],16) ^ int(key_code[j],16))
    j = j + 1
    if (j >= len(key_code)):
            j = 0


with open(output_file, "wb") as f:
    f.write(bytearray(decrypted))

