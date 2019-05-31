def is_number(x):
    try:
        int(x)
        return True
    except ValueError:
        return False

res = input()
if is_number(res):
    height = int(res)

height = 4

print(f"Height? Default = {height} ")

pyramid = ''

def half_row(n):
    return n * '#'

for i in range(1, height + 1):
    pyramid += (height - i) * ' ' + i * '#' + ' ' + i * '#' + '\n'



print(pyramid)


try:
    int(Y)
    Y = int(Y)
