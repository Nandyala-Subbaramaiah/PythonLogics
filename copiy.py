#shallow copy
import copy

original_list = [1, 2, [3, 4]]
shallow_copied_list = copy.copy(original_list)

shallow_copied_list[2][0] = 'Changed'

print("Original List: ", original_list)
print("Shallow Copied List: ", shallow_copied_list)


#deep copy import copy

import copy

original_list = [1, 2, [3, 4]]
deep_copied_list = copy.deepcopy(original_list)

deep_copied_list[2][0] = 'Changed'

print("Original List: ", original_list)
print("Deep Copied List: ", deep_copied_list)

