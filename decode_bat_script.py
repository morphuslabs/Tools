import re
import sys

if len(sys.argv) != 2:
    raise ValueError('Please provide the encoded file.')
   
encoded_file = sys.argv[1]

file = open(encoded_file, 'r')
data = file.readlines()
file.close()

regex = "set\s(\w{7})=(\S)"

alphabet = {}

for line in data:
    result = re.match(regex, line)
    if result:
        alphabet[result.group(1)] = result.group(2)

decoded_data = ""
for line in data:
    new_line = line
    for x,y in alphabet.items():
        new_line = (new_line.replace("%"+x+"%", y))
    decoded_data = decoded_data + new_line

print (decoded_data)
