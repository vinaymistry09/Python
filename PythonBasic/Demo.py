values =[1,2,"Vinay",4,5]

print(values[0])
print(values[1])

print(values[-1])
print(values[1:3])
values.insert(3,"Mistry")
print(values)
values.append("End")
print(values)

values[2] ="VINAY"
print(values)

del values[0]
print(values)

#tuple
val = (1,2,"vinay",4,5)

print(val[1])
#val[2] ="VINAY"
print(val)

#Dictionary

dic = { "a":2 , 4 : "abcd", "c":"efg"}
print(dic)
print(dic["a"])
print(dic[4])