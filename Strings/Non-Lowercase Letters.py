user_input = input()
# notlower_count = 0

# for i in user_input:
#   if i.islower() == False:
#     notlower_count += 1

# print(notlower_count)

counter = 0

for c in user_input:
  if c.isdigit():
    counter += 1
  else:
    if c.isalpha() and c.isupper():
      counter += 1

print('%s has %d non lowercased characters' % (user_input, counter))