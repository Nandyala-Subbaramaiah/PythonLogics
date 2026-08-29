lis1=[1,2,3,4,5]
new_list=[num for num in lis1 if num%2==0]
print(new_list)


def flatten_list(nested_list):
    flatten = []
    for item in nested_list:
        if isinstance(item, list):
            flatten.extend(flatten_list(item))
        else:
            flatten.append(item)
    return flatten
    
list1 = [1, [2], [3], [[[4]], [5]]]
output = flatten_list(list1)
print(output)

def total_sum_of_nested(nested_list):
    total_sum=0
    for item in nested_list:
        if isinstance(item, list):
            total_sum += total_sum_of_nested(item)
        else:
            total_sum+=item
    return total_sum

list1 = [1, [2], [3], [[[4]], [5]]]
output = total_sum_of_nested(list1)
print(output)

def count_element_in_list(nested_list):
    count_elements=0
    for item in nested_list:
        if isinstance(item, list):
            count_elements +=count_element_in_list(item)
        else:
            count_elements+=1
    return count_elements
list1 = [1, [2], [3], [[[4]], [5]]]
output = count_element_in_list(list1)
print(output)