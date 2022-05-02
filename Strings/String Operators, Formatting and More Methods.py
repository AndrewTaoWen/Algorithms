#String Operations
+ # connects two strings

* # multiplies string by x number of times

[x] # character at given index position

[x:y] # characters between given index range

[x:y:z] # every z characters between given index range

in
not in
# chekcs if string is within string

#String Formatting Operators
#formats output of strings

%c # character
%S # string
%d # decimals
%f # floating point
%g # for all digits

pi = 3.14159

print('%.2f' % pi)
#returns 3.14

print('%g' % pi)
#returns 3.14159
# supports up to 6 deimals, will round last decimal

print('%.3f' % pi)
#output 3.142

print('%.3g' % pi)
#outputs 3.14

#String Methods
variable_name.strip()
#trims off leading and trailing white spaces

variable_name.lstrip()
#only trims off leading white spaces

variable_name.rstrip()
#only trims of trailing white spaces

#word.replace(any characater, character in string, limit)

#replaces character in string with any character
# limit applies a limit to the number of times the builtin function is executed

#checks if string starts or ends with string x between index interval y, z
# print(word.startswith(x, y, z))
# print(word.endswith(x, y, z))
# returns true or false

#'x', join(y)
# puts x between every character in string y

#split()
#splits string

