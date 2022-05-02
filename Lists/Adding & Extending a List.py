a_list = [2,3,5,7,11,13]

b_list = a_list.copy()
#if .copy() function is not used, then b_list will include the changes made to a_list

a_list.append(17)

print(a_list)

print(b_list)