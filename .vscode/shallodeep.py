import copy

#shallow copy
original = [[1, 2], [3, 4]]

shallow = copy.copy(original)

shallow[0][0] = 100                 

print("Original:", original) 
print("Shallow :", shallow)

"""original ──→ [ outer list ]--->memory address and store the reference of inner list
                 ↓
    [1, 2]  ←── shallow --------->shallow list reference of inner list and reads elements from original list
    [3, 4]
Memory

Address 1000
┌─────────────────┐
│ original list   │
│ [2000, 3000]    │
└─────────────────┘
       ↓
       ↓
Address 2000              Address 3000
┌───────────┐             ┌───────────┐
│ [1, 2]    │             │ [3, 4]    │
└───────────┘             └───────────┘
"""


#deep copy
original = [[1, 2], [3, 4]]

deep = copy.deepcopy(original)

deep[0][0] = 100

print("Original:", original)
print("Deep    :", deep)

"""Original objects              Deep-copy objects

Address 1000                  Address 4000
┌──────────────┐              ┌──────────────┐
│ original     │              │ deep         │
│ [2000,3000]  │              │ [5000,6000]  │
└──────────────┘              └──────────────┘
      │                              │
      ▼                              ▼
Address 2000                  Address 5000
┌───────────┐                 ┌───────────┐
│ [1,2]     │                 │ [1,2]     │
└───────────┘                 └───────────┘

Address 3000                  Address 6000
┌───────────┐                 ┌───────────┐
│ [3,4]     │                 │ [3,4]     │
└───────────┘                 └───────────┘
"""