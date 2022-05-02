input_One = int(input())
input_Two = int(input())

start = min(input_One, input_Two)
end = max(input_One, input_Two)

while start <= end:
  if start % 2 == 0:
    print(start, 'even')
  else:
    print(start, 'odd')
  start += 1
