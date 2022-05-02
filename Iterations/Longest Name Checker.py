# longestNameLen = 0
# longestName = ''

# while True:
#   user_input = input()

#   if user_input == 'x':
#     print(longestName)
#     break
#   else:
#     if len(user_input) > longestNameLen:
#       longestName = user_input
#       longestNameLen = len(user_input)
#     else:
#       continue

user_input = ''
longest_name = ''

while user_input != 'x':
    user_input = input()

    if len(user_input) > len(longest_name) and user_input != 'X':
        longest_name = user_input

print('The longest name is:', longest_name)