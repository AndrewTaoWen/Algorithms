user_input = input()
print(user_input[::-1])

word = input()

reverse_word = ''

for i in range(-1, -1*len(word)-1, -1):
  reverse_word += word[i]

print('%s reversed is %s' % (word, reverse_word))

