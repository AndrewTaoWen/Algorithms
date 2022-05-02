countV = 0
countC = 0

user_input = input()

vowels = ['a','e','i','o','u']

for i in range(len(user_input)):
  if i.lower in vowels:
    countV += 1
  else:
    countC += 1

print('vowels:', countV)
print('consonants:', countC)

