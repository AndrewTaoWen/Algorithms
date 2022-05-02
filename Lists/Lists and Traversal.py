# num = int(input())

# even_nums = []

# for i in range(2, num+1, 2):
#   even_nums.append(i)

# print(even_nums)

# even_numbers = list(range(2,num+1,2))

# print(even_numbers)

size = int(input())

arr = []

for i in range(size):
  arr.append(int(input()))

if arr[0] == 6 or arr[-1] == 6:
  print('True')