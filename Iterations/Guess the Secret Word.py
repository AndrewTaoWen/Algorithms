# secret_word = input()

# while True:
#   guess = input()

#   if guess == secret_word:
#     print('you guessed it right')
#     break
#   else:
#     print('good try, but you were wrong')
#     continue

secret = 'secret'

user_input = ''

while user_input != secret:
  user_input = input('guess the secret word:')
print('you guessed it correctly')