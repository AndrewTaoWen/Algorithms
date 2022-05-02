# marks = []

# while True:
#   x = input()

#   if x == '':
#     break
#   else:
#     marks.append(int(x))

# print(sum(marks)/len(marks))

loop_flag = True
total_sum = 0
ctr = 0

while loop_flag:
    current_mark = int(input('Enter your mark between 0 to 100: '))
    total_sum += current_mark
    ctr += 1

    exit_input = input('do you want to exit?')

    if exit_input in 'Yy':
        loop_flag = False

average = total_sum / ctr

print('The average is:', average)