weekend = input()
num_acorns = int(input())

if weekend == 'Y':
  print('successful')
else:
  if num_acorns >= 40 and num_acorns <= 60:
    print('successful')
  else:
    print('unsuccessful')