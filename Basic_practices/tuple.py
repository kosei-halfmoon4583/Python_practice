# __coding: UTF-8 __

a = [2012, 2013, 2014]
b = (2012, 2013, 2014)

print(a)
print(b)

print(a[1])
print(b[1])

# listは、list内の要素の変更が可能、tupleは、変更不可
a[1] = 2016
print(a)

# b[1] = 2016
# print(b)

a.append(2015)
print(a)

# b.append(2015)
# print(b)

