num = int(input())

for i in range(1, num+1):
  print('*'*i)

pattern =''

for i in range(num):
  pattern += "*"
  print(pattern)

print('------')

pattern2 = '*'
for j in range(1, num+1):
  print(pattern2*j)