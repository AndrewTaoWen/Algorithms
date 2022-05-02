age = int(input())

print('all ages can enjoy G')

if age >= 18:
  print('you can watch all movies')
elif 13 <= age:
  print('you can watch all moveis except those which are R')
else:
  print('you can enjoy PG-13 with parents')