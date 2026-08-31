arr=[10,20,30,40,50]

target=30

left=0
right=len(arr)-1

while left<=right:
    mid=(left+right)//2

    if arr[mid]==target:
        print("Element found at index:",mid)
        break
    elif arr[mid]<target:
        left=mid+1
    else:
        right=mid-1

# BST RULES
#     30
#     /\ 
#   20  40
#   /\    \
# 10 25   50


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
def find_min(root):
    while root.left is not None:
        root = root.left
    return root.value

def find_max(root):
    while root.right is not None:
        root = root.right
    return root.value

root=Node(30)
root.left=Node(20)
root.right=Node(40)
root.left.left=Node(10)
root.left.right=Node(25)
root.right.right=Node(50)

print("minimum", find_min(root))
print("minimum", find_max(root))