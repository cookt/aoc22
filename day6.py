file = open("day6_input.txt", 'r')
count = 0
packet_len = 14
chars = []
for f in file.read():
    count += 1
    if len(chars) == packet_len:
        chars.pop(0)
    chars.append(f)
    if len(set(chars)) == packet_len:
        break
print(count)