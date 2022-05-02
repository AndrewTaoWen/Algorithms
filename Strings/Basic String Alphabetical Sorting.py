word = input('Enter a word')

word_copy = word
sorted_word = ''

while word:
  smallest_character = min(word)
  count = word.count(smallest_character)
  sorted_word += smallest_character * count
  word = word.replace(smallest_character, '')
print('sorted is', sorted_word)
