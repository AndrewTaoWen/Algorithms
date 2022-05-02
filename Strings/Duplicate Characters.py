# user_input = input()
# most_count = 0
# most = ''
# duplicate_letters = {}

# for i in user_input:
#   if user_input.count(i) > most_count:
#     duplicate_letters[i] = 1
#     most_count = user_input.count(i)
#     most = i

# for i in duplicate_letters:
#   print(i)
# print('most seen is:', most)

word = input()

duplicates = ''
most_used_letter = ''
counter = 0

for c in word:
    current_count = word.count(c)
    if current_count >= 2 and c not in duplicates:
        duplicates += c

    if current_count >= counter:
        counter = current_count
        most_used_letter = c

print(duplicates)
print('The most used character in %s is %s') % (word, most_used_letter)



