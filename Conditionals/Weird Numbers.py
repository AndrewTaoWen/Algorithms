user_input = int(input())

if user_input % 2 != 0:
  print('Weird')
else:
  if 6 <= user_input <= 20:
    print('Weird')
  else:
    print('Not Weird')