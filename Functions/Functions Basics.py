def functionName(arg1, arg2, arg3):
    ''' function docString: state purpose here

    arguments:
    -- arg1 : explanation
    -- arg2 : explanation
    -- arg3 : explanation

    return:
    -- value : explanation
    '''

    # write code inside the function here

    return value
# end of functionName()

def areaCircle(radius, pi):
    ''' areaCirlce() is a function that calculates the area of a circle

    arguments:
    -- radius : floating point value
    -- pi : floating point value

    return:
    -- area : the resulting area from the given arguments
    '''

    area = pi * (radius ** 2)

    return area
# end of areaCircle

my_radius = 6
pi = 3.14159

my_circle_area = areaCircle(my_radius, pi)
my_circle_area2 = areaCircle(my_radius, 3.14)

print('The area of my circle is %.4f units squared.' % my_circle_area)
print('The area of my circle with pi of 3.14 is %.4f units squared.' % my_circle_area2)