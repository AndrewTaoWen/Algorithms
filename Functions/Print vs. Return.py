def averagePrint1(array):
    ''' averagePrint1() outputs the total average of all the integers in a list

    argument:
    -- array : a list of integers
    '''

    total_sum = sum(array)
    length = len(array)
    average = total_sum / length

    print('The average of the given list of values is:', average)
# end of averagePrint1

def averagePrint2(array):
    ''' averagePrint() returns the total average of all the integers in a list

    argument:
    -- array : a list of integers
    '''

    total_sum = sum(array)
    length = len(array)
    average = total_sum / length

    return average
# end of averagePrint2

# Start of the actual program

values = [96, 42, 55, 4, 12, 14, 67, 25, 37, 82, 62, 13]

print('Executing avereagePrint1():')
averagePrint1(values)
print('Executing avereagePrint2():')
averagePrint2(values)
print('-'*25)

print('Setting variables result1:')
result1 = averagePrint1(values)
print('Setting variables result2:')
result2 = averagePrint2(values)

print('-'*25)
print('Variable result1:', result1)
print('Variable result2:', result2)

