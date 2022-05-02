import math

s1 = input()
s2 = input()
s3 = input()

planks = len(s1) + len(s2) + len(s3)

boxes_paint = math.ceil(planks / 12)

leftover = boxes_paint*12 - planks

total_cost = boxes_paint * 14.95

print('There are', planks, 'paint cans needed')

print('There are,' , leftover, 'paint cans leftover')

print('Total cost:', total_cost)