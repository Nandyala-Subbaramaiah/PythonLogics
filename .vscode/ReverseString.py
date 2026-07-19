#String Reverse Pogramming
'''str="subbu is python developer"
words=str.split(" ")
print(words)

words=words[-1::-1]
print(words)
outstr=' '.join(words)
print(words)

#RemoveDuplicatesInString
s='AABBCD'
OUtPUT=''
for ch in s:
   if ch not in OUtPUT:
       OUtPUT=OUtPUT+ch
print(OUtPUT) 
#RemoveDuplicatesInStringList
s='SSDBASB'
list=[]
for ch in s:
    if ch not in list:
        list.append(ch)
Op=''.join(list) 
print(Op)
#RemoveDuplicatesInStringSets
s='AABBSDAG'
s2=set(s)
Output=''.join(s2)
print(Output)

s='NAMAN'
reverse=(s[::-1])
if reverse==s:
    print('palindrom')
else:
    print("Not Palindrom")
    
stri="python programming"
s=stri.split()[::-1]
l=[]
for i in s:
    l.append(i)
    print(" ".join(l))
    
rep="subbu"
re=rep.replace('u', '')
print(re)

rev='subbu'
new_rev=rev.replace("subbu","RJN")
print(new_rev)

rs='Good Morning'
sr=rs.replace("Good","Greate")
print(sr)


string = "grrks FOR grrks"
new_string = string.replace("r", "e" )

print(string)
print(new_string)

ste="geeks for geeks \ngeeks for geeks"
print(ste)
print(ste.replace("geeks", "geeks for geeks"))

strange='geeks for geeks geeks geeks geeks'
print(strange.replace("e","a"))
print(strange.replace("ek", "a", 5))

#using list comprehension & replace()
list1=["fruites","apples","bananna"]
#list2=[i.replace("apples","oranges")for i in list1]
list3=list(map(lambda i:str.replace(i,'bananna','grape'),list1))
print(list3)





# Original list
words = ["Python", "JAVA", "DEVELOPER"]

# Reversing the list
reversed_words = words[::-1]

print(reversed_words)


def revrse(reverse):
  new_rev=reverse[::-1]
  return new_rev

reverse=["subbu", "rama"]
print(revrse(reverse))

lst=[54,54,78]

l=[]

for i in lst:
    
    l.insert(0, i)
    
print(l)


lst = [10, 11, 12, 13, 14, 15,11]
print("Using reversed() ", list(reversed(lst)))



str="subbu"
newstr=str[::-1]  
for i in newstr:
    break
print(newstr)

list1=["Pytho","jango","developer"]
newlist=list1[::-1]
result=" ".join(newlist)
print(result)

str="subbu is python developer"
words=str.split(" ")
print(words)

words=words[::-1]
print(words)
outstr=" ".join(words)
print(words)


#String occurance using counter and re
from collections import Counter
import re


String="Javatpoint in a wesite"

count=0
for i in String:
    if i=='a':
        
        count=count+1
print("count of given string 'a': "+str(count))
        
counter=String.count('a')
print("count of number of string : "+str(counter))

#count=Counter(String)
count = len(re.findall("e",String))
print(str(count))


#countoff using operator
import operator as op 
str_str="GeeksForGeeks"
counter=op.countOf(str_str,"e")
print("e: ",str(counter))


import operator as op 
str_str="subbu"
print("s:",op.countOf(str_str,"s"))
print("u:",op.countOf(str_str,"u"))
print("b:",op.countOf(str_str,"b"))




def swap(newlist):
    size=len(newlist)
    
    temp=newlist[0]
    newlist[0]=newlist[-2]
    newlist[-2]=temp
    return newlist  

newlist=["subbu","rama","in"]
print(swap(newlist))

string_reverse="in"
nlist=[]
for i in newlist:
    if i==string_reverse:
        nlist.append(i[::-1])
    else:
        nlist.append(i)
print(nlist)
'''

"""newlist=["I","studied","in","Tirupati"]
string_reverse="studied"
nlist=[]
for i in newlist:
    if i==string_reverse: 
        nlist.append(i[::-1])
    else:
        nlist.append(i)
print(nlist)


string="I studeid in tirupati"
newstr=string
words=newstr[::-1]
words=' '.join(words)
print(words)




#Count in string
count=0
for i in words:
    count+=1
print(count)


#reverse in middle of the string 
def reverse_middle_section(s):
    words = s.split()
    beginning = words[0]
    if words[0] == "I":
        words = words[1:]
        
    middle = ' '.join(words[::-1])
    reversed_middle = middle[::-1]
    
   # end=words[-1] 
    reversed_string = beginning + ' ' + reversed_middle
    return reversed_string
string = "I studeid in tirupati"
reversed_string = reverse_middle_section(string)
print(reversed_string)  

def reverse_vowels(s):
    vowels = "aeiouAEIOU"
    
    # Extract the vowels from the string
    vowel_list = [char for char in s if char in vowels]
    
    # Reverse the list of vowels
    vowel_list.reverse()
    
    # Replace the vowels in the string with the reversed vowels
    result = []
    for char in s:
        if char in vowels:
            result.append(vowel_list.pop(0))
        else:
            result.append(char)
    
    return ''.join(result)

# Example usage
input_string = "oranges"
output_string = reverse_vowels(input_string)
print(output_string)  


import string

def count_characters(s):
    letters = set(string.ascii_letters)
    digits = set(string.digits)
    
    upper_count = 0
    lower_count = 0
    digit_count = 0
    special_count = 0
    
    for char in s:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1
        elif char in digits:
            digit_count += 1
        else:
            special_count += 1
    
    return upper_count, lower_count, digit_count, special_count

# Example usage
text = "Hello, World! 2024 #Python"
upper, lower, digits, special = count_characters(text)
print(f"Uppercase letters: {upper}")
print(f"Lowercase letters: {lower}")
print(f"Digits: {digits}")
print(f"Special characters: {special}")

#trying to find the index of a specific character in a string
text = "hello"
index = text.index("o")  # returns 2 (first occurrence)
print(index) 


#find the index of characters in a string without using any inbuilt methods?
s = "hello"
target = 'l'
found = False
i = 0

for char in s:
    if char == target:
        print("First occurrence of", target, "is at index", i)
        found = True
        break
    i += 1

if not found:
    print("Character not found")

words="python backend developer"
count=0
for i in words:
    count+=1
print(">>>>>>>>>>>>>>>", count)
">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<"
">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"

def reverse_vowels(s):
    vowels = "aeiouAEIOU"
    
    # Extract the vowels from the string
    vowel_list = [char for char in s if char in vowels]
    
    # Reverse the list of vowels
    vowel_list.reverse()
    
    # Replace the vowels in the string with the reversed vowels
    result = []
    for char in s:
        if char in vowels:
            result.append(vowel_list.pop(0))
        else:
            result.append(char)
    
    return ''.join(result)

# Example usage
input_string = "oranges"
output_string = reverse_vowels(input_string)
print(output_string)  

#Python program that compresses a string by counting consecutive repeating characters — like turning "aaabbcc" into "3a2b2c"
def compress_string(s):
    if not s:
        return ""
    
    result = []
    count = 1
 
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            count +=1
        else:
            result.append(f"{count}{s[i-1]}")
            count = 1
    result.append(f"{count}{s[-1]}")
    return "".join(result)
  
input_string = "aaabbcc"
print(compress_string(input_string))  # Output: "3a2b2c"
"""
                        
def reverse_vowels(s):
    vowels = "aeiouAEIOU"


    s="oranges"
    vowels_list = [char for char in s if char in vowels]
    vowels_list.reverse()

    result = []

    for char in s:
        if char in vowels:
            result.append(vowels_list.pop(0))
        else:
            result.append(char)
    return ''.join(result)
input_string = "oranges"
output_string = reverse_vowels(input_string)
print("reversed vowels was: ", output_string)  

