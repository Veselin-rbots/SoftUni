line = input()

current_result = ''
result = ' '

for char in line :
    if not char.isdigit():
        current_result += char
    else:
        current_result = current_result.upper() * int(char)
        result += current_result
        current_result = ''

print(f'Unique symbols used : {len(set(result))}')
print(result)