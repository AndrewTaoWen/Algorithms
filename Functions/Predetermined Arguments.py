def distance(x, y, a=0,b=0):
    ''' distance() calculates the distance between point(x,y) and point(a,b).
    If point(a,b) is not specified, it will calculate the distance from the origin to point(x,y)

    Distance Formula: https://www.khanacademy.org/math/geometry/hs-geo-analytic-geometry/hs-geo-distance-and-midpoints/v/distance-formula

    arguments:
    -- x : numeric
    -- y : numeric
    -- a : numeric
    -- b : numeric

    return
    -- distance in units
    '''

    delta_x = a - x
    delta_y = b - y

    result = (delta_x ** 2 + delta_y ** 2) ** 0.5

    return result
# end of distance()

print('Distance from (3,4) to (10,13) is %f units.' % distance(3, 4, 10, 13))
print('Distance from (5,12) from the origin is %f units.' % distance(5,12))
print('Distance from (1,1) to (5,5) is %f units' % distance(x=1, y=1, a=5, b=5))

