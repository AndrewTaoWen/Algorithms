a = int(input())
b = int(input())
c = int(input())

if a > b:
  d=a
  e=b
  if d > e:
    print(a)
  elif c < d:
    print(b)
  else:
    print(c)
else:
  if c > b:
    print(b)
  elif c < a:
    print(a)
  else:
    print(c)