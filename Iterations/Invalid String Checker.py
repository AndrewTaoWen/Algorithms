# prohibited_characters = ['1','2','3','4','5','6','7','8','9','0','!','@','%','$','^','&','*']

# user_input = input()

# for i in prohibited_characters:
#   if i in user_input:
#     print('this is invalid')
#     break
# else:
#   print('valid')

valid = False

while not valid:
    user_input = input('')

    if '1' in user_input:
        valid = False

    elif '2' in user_input:
        valid = False

    elif '3' in user_input:
        valid = False

    elif '4' in user_input:
        valid = False

    elif '5' in user_input:
        valid = False

    elif '6' in user_input:
        valid = False

    elif '7' in user_input:
        valid = False

    if '8' in user_input:
        valid = False

    elif '9' in user_input:
        valid = False

    elif '0' in user_input:
        valid = False

    elif '@' in user_input:
        valid = False

    elif '!' in user_input:
        valid = False

    elif '%' in user_input:
        valid = False

    elif '$' in user_input:
        valid = False

    elif '^' in user_input:
        valid = False

    elif '&' in user_input:
        valid = False

    elif '*' in user_input:
        valid = False

    else:
        valid = True

print(user_input, 'is valid.')