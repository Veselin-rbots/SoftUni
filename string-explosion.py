line = input()

index = 0
strength = 0

while index < len(line):
    if line[index] == '>':
        strength += int(line[index+1])
        index += 1
        while not line[index] == '>' and strength:
            line = line.replace(line[index], "", 1)
            strength -= 1
    else:
        index += 1

print(line)
# for index in range(len(line)-1):
#     if line[index] == line[index + 1]:
#         line = line.replace(line[index], "")