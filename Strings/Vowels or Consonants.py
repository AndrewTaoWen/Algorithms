# vowels = ['a','e','i','o','u']
# user_input = input()
# num_vowels = 0

# for i in user_input:
#   if i in vowels:
#     num_vowels += 1

# if num_vowels > (len(user_input)/2):
#   print('More vowels')
# else:
#   print('More consonants')

user_input = input()

vowel_counter = 0
consonant_counter = 0

vowel_counter += user_input.count('a')
vowel_counter += user_input.count('e')
vowel_counter += user_input.count('i')
vowel_counter += user_input.count('o')
vowel_counter += user_input.count('u')

consonant_counter = len(user_input) - vowel_counter

if consonant_counter > vowel_counter:
  print('more consonant')
elif consonant_counter == vowel_counter:
  print('same amount')
else:
  print('more vowels')
