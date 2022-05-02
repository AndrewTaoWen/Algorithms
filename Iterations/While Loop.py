user_input = int(input())

factor = 1

while factor <= user_input:
  if user_input % factor == 0:
    print(factor)
  factor += 1

