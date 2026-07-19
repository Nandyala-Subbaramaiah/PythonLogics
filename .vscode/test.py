list1=[1,2,3,4,5]
list1.pop(2)
print("removing the lement based on the index:",list1)
list1.insert(2,3)
print("insrt the lement:",list1)
list1.remove(5)
print("removing element",list1)
del list1[2]
print("deleting the element",list1)

#list1.clear()
print(list1)
list1=[1,2,3,4,5,6,7,8,9,10]
squ_qub=[num**2 if num%2==0 else num**3 for num in list1]
print(squ_qub)

