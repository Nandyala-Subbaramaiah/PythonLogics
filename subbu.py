"""def rearrange_list(nums):
    odd_numbers = [num for num in nums if num % 2 != 0] [::-1]
    odd_index = 0
    result = []
    
    for num in nums:
        if num % 2 == 0:
            result.append(num)
        else:
            result.append(odd_numbers[odd_index])
            odd_index += 1
            
    return result

list1=[1,2,11,4,5,6,7,8,19,10]
print_even_odd=rearrange_list(list1)
print(print_even_odd)"""
def max_subarray_sum(nums):
    max_sum = float('-inf')
    current_sum = 0
    start = end = temp_start = 0
    
    for i in range(len(nums)):
        if current_sum <= 0:
            current_sum = nums[i]
            temp_start = i
            
        else:
            current_sum += nums[i]
            
        if current_sum > max_sum:
            max_sum =current_sum
            start = temp_start
            end = i
            
    return max_sum, nums[start:end+1]
    
    
input_list = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
output_sum, output_subarray = max_subarray_sum(input_list)

print("Largest Sum:", output_sum)
print("Subarray:", output_subarray)