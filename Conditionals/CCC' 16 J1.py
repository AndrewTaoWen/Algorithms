c = []
b = 0

for _ in range (6):
  c += input()

for i in c:
  if i == 'W':
    b += 1

if b >= 5:
    print('1')
elif b == 3 or b == 4:
    print('2')
elif b == 1 or b == 2:
    print('3')
else:
    print('-1')