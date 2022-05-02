day = int(input())
evening = int(input())
weekend = int(input())

a_day_cost = max(day - 100, 0) * 0.25

a_evening = 0.15 * evening
a_weekend = 0.20 * weekend

b_day_cost = max(day - 250, 0) * 0.45
b_evening = 0.35 * evening
b_weekend = 0.25 * weekend

plan_a_total = round(a_day_cost + a_evening + a_weekend, 2)
plan_b_total = round(b_day_cost + b_evening + b_weekend, 2)

print(plan_a_total, plan_b_total)

if plan_a_total > plan_b_total:
    print('Plan B is cheapest.')
elif plan_a_total < plan_b_total:
    print('Plan A is cheapest.')
else:
    print('Plan A and B are the same price.')

# a = int(input())
# b = int(input())
# c = int(input())

# if ((a-100) > 0):
#   costA = round((0.25 * (abs(a-100))) + (0.15 * (b)) + (0.2 * (c)), 2)
# else:
#   costA = round((0.15 * (b)) + (0.2 * (c)), 2)

# if ((a-250) > 0):
#   costB = round((0.45 * (abs(a-250))) + (0.35 * (b)) + (0.25 * (c)), 2)
# else:
#   costB = round((0.35 * (b)) + (0.25 * (c)), 2)

# print('Plan A costs ' + str(costA))

# print('Plan B costs ' + str(costB))

# if costA > costB:
#   print('Plan B is cheapest.')
# elif costA < costB:
#   print('Plan A is cheapest.')
# else:
#   print('Plan A and B are the same price.')