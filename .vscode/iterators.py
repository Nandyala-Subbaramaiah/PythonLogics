"""s="GFG"
it=iter(s)
print(next(it))
print(next(it))
print(next(it))

#iterate tems in list using iterator
# Create a list
my_list = [1, 2, 3, 4, 5]

# Create an iterator from the list
my_iterator = iter(my_list)

# Iterate through the list using the iterator
while True:
    try:
        # Get the next item
        item = next(my_iterator)
        print(item)
    except StopIteration:
        # If StopIteration is raised, break from the loop
        break

 #dictionary   
dict={1,2,42,6,8}
me_iterator=iter(dict)
while True:
    try:
        items=next(me_iterator)
        print(items)
    except StopIteration:
        break
 
    
tuple=(3,2,1,5,7,4)
iteratior=iter(tuple)
while True:
    try:
        itemm=next(iteratior)
        print(itemm)
    except StopIteration:
        break

#iterable
lit1=[2,4,5,6,7]

for i in lit1:
    print(i)
    
#iterator each and every element at one time using iterator and next methods
#its helping for memory efficient
iterator_elements=iter(lit1)
one_element_iterator=iterator_elements.__next__()
print(one_element_iterator)
   """
