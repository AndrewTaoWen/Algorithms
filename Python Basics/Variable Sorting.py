total_cost = float(input('Enter the meal cost: '))
tip_percentile = int(input('Enter the tip percentage as a whole number: '))

tip = total_cost * (tip_percentile /100)
total_cost += tip

print('The meal costs with the tip is:', total_cost)