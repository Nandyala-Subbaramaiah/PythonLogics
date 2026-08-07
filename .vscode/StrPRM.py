#remove the duplicates from the string
"""s='AABBCD'
OUtPUT=''
for ch in s:
   if ch not in OUtPUT:
       OUtPUT=OUtPUT+ch
print(OUtPUT) 

#method 2
s='SSDBASB'
list=[] 
for ch in s:
    if ch not in list:
        list.append(ch)
Op=''.join(list)
print(Op)

#method 3
s='AABBSDAG'
s2=set(s)
Output=''.join(s2)
print(Output)


#PALINDROM STRING 
s='NAMANff'
reverse=(s[::-1])
if reverse==s:
    print('palindrom')
else:
    print("Not Palindrom")
    



#reverse in middle of the words in string 
def reverse_middle_section(s):
    words = s.split()  # Split the string into words
    if words[0] == "I":  # Check if the first word is "I"
        beginning = words[0]  # Keep the first word as the beginning
        middle = words[1:]  # Take the rest as the middle section
    else:
        beginning = ""
        middle = words

    # Reverse the middle section
    reversed_middle = ' '.join(middle[::-1])
    
    # Combine beginning and reversed middle
    if beginning:
        reversed_string = beginning + ' ' + reversed_middle
    else:
        reversed_string = reversed_middle

    return reversed_string

string = "I studied in Tirupati"
reversed_string = reverse_middle_section(string)
print(reversed_string)


from collections import Counter
import re 


String="Javatpoint in a wesite"

count=0
for i in String:
    if i=='a':
        
        count=count+1
print("count of given string 'a': "+str(count))
        
counter=String.count('a')
print("count of number of string a: "+str(counter))"""

"""
#string occorances
Str="subbu"
res={}

for i in Str:
    if i not in res:
        res[i]=1
    else: 
        res[i]+=1
print(res)



#revered sentances
#reversed word in given string
str="python developer"
new_str=str.split()
reversed_str=' '.join(reversed(new_str))
print(reversed_str)


#method2
str="subbu is python developer"
words=str.split(" ")
words=words[::-1]
print(words)
outstr=" ".join(words)
print(words)


# method one Original string reversed here 
original_str = "python developer"
reversed_str = ""
 
# Use a for loop to iterate over the string in reverse order
for i in range(len(original_str) - 1, -1, -1):  -#start stop step 
    reversed_str = reversed_str+original_str[i]
print(reversed_str)

#method2
# Original string
original_str = "python developer"

# Convert the string to a list of characters
char_list = list(original_str)

# Reverse the list of characters
char_list.reverse()

# Join the reversed list of characters back into a string
reversed_str = ''.join(char_list)

print(reversed_str)
"""
"""#method 1
#counting words in a string
def count_words(cwords):
    cwords=cwords.split()
    cowords=len(cwords)
    return cowords
     
    
cwords="Subbu is good boy"
res=count_words(cwords)
print("count words in a string: ",res)

#method2
def count_words(s):
    # Initialize count and in_word variables
    count = 0
    in_word = False

    for char in s:
        if char.isspace():
            in_word = False
        elif not in_word:
            count += 1
            in_word = True
   
    return count

# Example usage
string = "python developer"
word_count = count_words(string)
print(f"The number of words in the string is: {word_count}")

def count_letters(s):
    upper = 0
    lower = 0
    number = 0
    special = 0
    
    for char in s:
        if char.isupper():
        upper += 1
        elif char.islower():
            lower += 1
        elif char.isdigit():
            number += 1
        else:
            special += 1
            
    return upper, lower, number, special

# Example usage
strr = "Subbu@1122"
res = count_letters(strr)
print(f"Uppercase letters: {res[0]}")
print(f"Lowercase letters: {res[1]}")
print(f"Numbers: {res[2]}")
print(f"Special characters: {res[3]}")

#sorting 0s ,1s method 1
def convert_binary_string(binary_str):
    # Convert the string to a list
    binary_list = [char for char in binary_str]
    
    # Initialize counters for 0s and 1s
    count_0 = 0
    count_1 = 0
    
    # Count the number of 0s and 1s
    for char in binary_list:
        if char == '0':
            count_0 += 1
        elif char == '1':
            count_1 += 1
    
    # Create the output list with the appropriate number of 0s and 1s
    result_list = ['0'] * count_0 + ['1'] * count_1
    
    # Convert the list back to a string
    result_str = ''
    for char in result_list:
        result_str += char
    
    return result_str

# Example usage:
x = "01010011"
output = convert_binary_string(x)
print(output)  # Output: "00001111"


#method 2
def convert_b  inary_string(binary_str):
    # Count the number of 0s and 1s
    count_0 = binary_str.count('0')
    count_1 = binary_str.count('1')
    
    # Create the result string with the appropriate number of 0s and 1s
    result_str = '0' * count_0 + '1' * count_1
    
    return result_str

# Example usage:
x = "01010011"x
output = convert_binary_string(x)
print(output)  # Output: "00001111"

def longest_repeated_substring_brute_force(s):
    if not s:
        return "", 0 
    
    max_length = 0
    max_substring = ""

    for i in range(len(s)):
        for j in range(i, len(s)):
            # Get the current substring
            substring = s[i:j+1]
            # Check if all characters in the substring are the same
            if all(char == substring[0] for char in substring):
                # Update the longest substring if necessary
                if len(substring) > max_length:
                    max_length = len(substring)
                    max_substring = substring
    
    return max_substring, max_length

# Example usage:
s = "aaabbbccddeeeffffgggg"
longest_substring, length = longest_repeated_substring_brute_force(s)
print(f"The longest repeated substring is: '{longest_substring}' with length {length}")

def count_letters(s):
    upper = 0
    lower = 0
    number = 0
    special = 0
    
    for char in s:
        if char.isupper():
            upper += 1
        elif char.islower():
            lower += 1
        elif char.isdigit():
            number += 1
        else:
            special += 1
            
    return upper, lower, number, special

# Example usage
strr = "Subbu@1122"
res = count_letters(strr)
print(f"Uppercase letters: {res[0]}")
print(f"Lowercase letters: {res[1]}")
print(f"Numbers: {res[2]}")
print(f"Special characters: {res[3]}")
    
  
#find the length of the string
string="subbu"
find_len=len(string)
print(find_len)

#using count varible
count=0
for char in string:
    count+=1
print(count)
      

# Python code 
# To print even length words in string 

#input string 
n="This is a python language dfd"
#splitting the words in a given string
s=n.split(" ") 
for i in s: 
#checking the length of words
  if len(i)%2==0: 
      print(i)
    
"""
"""# Python program to accept the strings
# which contains all the vowels

# Function for check if string
# is accepted or not
def check(string) :

	string = string.lower()

	# set() function convert "aeiou"
	# string into set of characters
	# i.e.vowels = {'a', 'e', 'i', 'o', 'u'}
	vowels = set("aeiou")

	# set() function convert empty 
	# dictionary into empty set
	s = set({})

	# looping through each
	# character of the string
	for char in string :
    
		# Check for the character is present inside
		# the vowels set or not. If present, then
		# add into the set s by using add method
		if char in vowels :
			s.add(char)
		else:
			pass
			
	# check the length of set s equal to length 
	# of vowels set or not. If equal, string is 
	# accepted otherwise not
	if len(s) == len(vowels) :
		print("Accepted")
	else :
		print("Not Accepted")


# Driver code
if __name__ == "__main__" :
	
	string = "SiouqaeLs"

	# calling function
	check(string)"""

#voverls checking here 
"""def check(s):
    s = s.lower()  # Convert the string to lowercase
    
    vowels = set("aeiou")  # Create a set of vowels
    
    found_vowels = set()  # Initialize an empty set to store found vowels
    
    for char in s:
        if char in vowels:
            found_vowels.add(char)
    
    if len(found_vowels) == len(vowels):
        print("Accepted")
    else:
        print("Not Accepted")
    
    return found_vowels

# Example usage:
string = "SiouqaeLs"
checking_vowels = check(string)
print(checking_vowels)
    

def check_upper_lower_vowels(s): 
    # Define sets for vowels
    lower_vowels = set("aeiou")
    upper_vowels = set("AEIOU")
    
    # Initialize sets to store found vowels
    found_lower_vowels = set()
    found_upper_vowels = set()  
    
    # Loop through each character in the string
    for char in s:
        if char in lower_vowels:
            found_lower_vowels.add(char)
        elif char in upper_vowels:
            found_upper_vowels.add(char)
    
    return found_lower_vowels, found_upper_vowels

# Example usage
string = "Hello, How Are You Doing Today?" 
lower_vowels, upper_vowels = check_upper_lower_vowels(string)
print(f"Lowercase vowels: {lower_vowels}")
print(f"Uppercase vowels: {upper_vowels}")


# Sentence
string = "Hulkmaniacs are running wild in the whole world"
# Sentence splitted up into words
wordList = string.split() 
# Defining vowels for uppercase and lowercase
vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
#Traversing every word in wordList
for word in wordList:
    vowelCount = 0
    #Traversing every character of the word
    for i in range(0, len(word)):
        # If the word contains a vowel then vowelCount adds by 1
        if word[i] in vowels:
            vowelCount += 1 
    print("The word is", word, "and it contains", vowelCount, "vowels in it")

#longest sustring without repeating characters
def longest_unique_substring(s): 
    char_set = set()
    start = 0
    max_length = 0
    longest_substring = ""
    
    for end in range(len(s)):
        while s[end] in char_set:
            char_set.remove(s[start])
            start += 1
        char_set.add(s[end])
        current_length = end - start + 1
        if current_length > max_length:
            max_length = current_length 
            longest_substring = s[start:end+1]

    return longest_substring, max_length

# Example usage:
s = "abcabcbb"
longest_substring, length = longest_unique_substring(s)
print(f"The longest substring without repeating characters is: '{longest_substring}' with length {length}")


str="suubu"
res={
    
}
for char in str:
    if char not in res:
        res[char]=1
    else:
        res[char]+=1
        
        print(res)
    
    
    
def word_count_str(s):
    
    count=0
    in_word=False
    for char in s:
        if char.isspace():
            in_word=False
        elif not in_word:
            count+=1
            in_word=True
        
    return count

string="Python backend developer"
print_word_count=word_count_str(string)
print(print_word_count)

str="subbu is python developer"
words=str.split(" ")
words=words[::-1]
print(words)
outstr=" ".join(words)
print(words)

str="I am in tirupati"
chars_to_remove="ia"
str_filter=''.join([char for char in str if char not in chars_to_remove])
print(str_filter)

#method1
str="I am in tirupati"
vowels="aeiouAEIOU"
removing_vowels=str.translate(str.maketrans("","", vowels))
print(removing_vowels)

#method2
str="I am in tirupati"
vowels="aeiouAEIOU"
removing_vowels= ""
for char in str:
    if char not in vowels:
        removing_vowels+=char
print(removing_vowels)

#replace characters in a word 
str="I am in tirupati"
word=str.replace("i","c")
print(word)

#reverse a string without using any inbuilt methods
def check_palindrom(s):
    reversed_str = ""
    for char in s:
        reversed_str = char + reversed_str
    if reversed_str == s:
        print("Palindrome")
    else:
        print("Not a palindrome")

s = "naman"
check_palindrom(s)


def printing_longest_substring_without_repeating_characters_k(s):
    char_set=set()
    start=0
    max_length=0
    longest_sub_string=""  
    for end in range(len(s)):
       while s[end] in char_set:
           char_set.remove(s[start])
           start+=1
       char_set.add(s[end])
       current_length=end-start+1
       if current_length>max_length:
           max_length=current_length
           longest_sub_string=s[start:end+1]
           
    return longest_sub_string, max_length
       
    
s="abcabcbb"  
print_without_repeating_str=printing_longest_substring_without_repeating_characters_k(s)
print(print_without_repeating_str)
    
#Python program to check if a string has at least one letter and one number
s = "gfg123"
l=d =False
for char in s:
    if char.isalpha():
        l=True
    if char.isdigit():
        d=True
    if l and d:
        print(True)
        break
else:
    print(False)                                                                                                                                                                                                                        


#Using all()
#all() function checks if all vowels are present in the string. It returns True if every condition in the list comprehension is met.




s = "Geeksforgeeks"
v = 'aeiou'


# check if each vowel exists in the string
if all(i in s.lower() for i in v):
                             
    print("True")
else:            
    print("False") 
                    

s1 = "VISHAKSHI"
s2 = "VANSHIKA"

# find common characters
res= len(set(s1.lower()).intersection(set(s2.lower())))
print(res)


#removing duplicates in string 
s="subbu"

seen=set()
ans=""
for char in s:
    if char not in ans:
        seen.add(char)
        ans+=char
print(ans)

#another method
s="subbu"
ans=""
for char in s:
    if char not in ans:
        ans=ans+char
print(ans)

#extracting the value 
a = ["Kite", "Apple", "King", "Banana", "Kangaroo", "cat"]
K = 'K'
res=[word for word in a if word.startswith(K)]

print(f"Words starting with '{K}':", res)


#In this challenge, the user enters a string and a substring. 
# You have to print the number of times that the substring occurs in the given string. 
# String traversal will take place from left to right, not from right to left.Sample Input
#ABCDCDC CDC

def count_substring(string, sub_string):
     start=0
     end=len(sub_string)
     counter=0
     while end <= len(string):
        if sub_string==string[start:end]:
            counter+=1
        start+=1
        end+=1
     return counter
               
if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
    
#Python has built-in string validation methods for basic data.
#  It can check if a string is composed of alphabetical characters,
#  alphanumeric characters, digits, etc.
if __name__ == '__main__':


    s = input()  # Input string

    # Print True/False for each condition
    print(any(char.isalnum() for char in s))  # Check for alphanumeric characters
    print(any(char.isalpha() for char in s))  # Check for alphabetical characters
    print(any(char.isdigit() for char in s))  # Check for digits
    print(any(char.islower() for char in s))  # Check for lowercase characters
    print(any(char.isupper() for char in s))  # Check for uppercase characters




def unique_chars(word):
    char_count = {}  # Dictionary to store character frequencies

    # Counting occurrences manually
    for char in word:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    # Filtering out unique characters manually
    unique_list = []
    for char in word:  # Iterate in order to preserve original sequence
        if char_count[char] == 1:
            unique_list.append(char)

    return unique_list

word = "developer"
print(unique_chars(word))  # Output: ['v', 'l', 'r']


str1 = "listen"
str2 = "silent"

# Counting characters using a loop
char_count = {}

for char in str1:
    char_count[char] = char_count.get(char, 0) + 1

for char in str2:
    char_count[char] = char_count.get(char, 0) - 1

# If all values are 0, they are anagrams
print(all(value == 0 for value in char_count.values()))  # Output: True

#Anagrams 
from collections import defaultdict

def are_anagrams(s1, s2):
    freq1 = defaultdict(int)
    freq2 = defaultdict(int)

    for char in s1:
        freq1[char] += 1

    for char in s2:
        freq2[char] += 1

    return freq1 == freq2

print(are_anagrams("listen", "silent"))  # True
print(are_anagrams("hello", "world"))    # False


# original_str = "python developer"
# reversed_str = ""

# # Use a for loop to iterate over the string in reverse order
# for i in range(len(original_str) - 1, -1, -1):
#     reversed_str = reversed_str+original_str[i]
# print(reversed_str)

def unique_chars(word):
    char_count = {}  # Dictionary to store character frequencies

    # Counting occurrences manually
    for char in word:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1 

    # Filtering out unique characters manually
    unique_list = []
    for char in word:  # Iterate in order to preserve original sequence
        if char_count[char] == 1:
            unique_list.append(char)

    return unique_list

word = "developer"
print(unique_chars(word))  # Output: ['v', 'l', 'r']


def count_substring(string, sub_string):
     start=0
     end=len(sub_string)
     count=0
     while end <= len(string):
        if sub_string==string[start:end]:
            count+=1
        start+=1
        end+=1 
     return count
  
Str="ABCDCDC"
Sub_str="CDC"
count=count_substring(Str, Sub_str)
print(count)   
"""
"""strr="My name is subbaramaiah"
words=strr.split()
count_words={}
for word in words:
    count_chars = {} 
    for char in word:
        if char in count_chars:
            count_chars[char]+=1
        else:
            count_chars[char]=1
    count_words[word]=count_chars
print(count_words)

#Using replace() method
str1="  listen  "
removing_spaces=str1.replace(" ","")
print(removing_spaces)


#Removing Leading Spaces Only
s = "   Hello World"

s = s.lstrip()
print(s)

#Removing Trailing Spaces Only
s = "Hello World   "

s = s.rstrip()
print(s)

#Removing Leading and Trailing Spaces
s = "   Hello World   "

s = s.strip()
print(s)


def reverseString(s):
    res = []
  
    for i in range(len(s) - 1, -1, -1):
    #len(s) - 1 → start index (the last character of the string)

    # -1 → stop value (the loop runs until index 0, not including -1)

    # -1 → step value (means move backward by one each time)
        res.append(s[i])

    return ''.join(res)

if __name__ == "__main__":
    s = "abdcfe"
    print(reverseString(s))
 
s="ababca"
c="a"
s=s.replace(c,"")
print(s)

def count_substring(string, sub_string):
     start=0
     end=len(sub_string)
     count=0
     while end <= len(string):
        if sub_string==string[start:end]:
            count+=1
        start+=1
        end+=1  
     return count
  
Str="ABCDCDC"
Sub_str="CDC"
count=count_substring(Str, Sub_str)
print(count) 

def longest_unique_substring(s): 
    char_set = set()
    start = 0
    max_length = 0
    longest_substring = ""
    
    for end in range(len(s)):
        while s[end] in char_set: #abc/a/->b->c->a/b/->c->/a->b->c->/b->->
            char_set.remove(s[start]) #start[0],[1],[2],[3],[4],[5],[6] If any duplicate removed(old value) then only increase the start +1 
            start += 1
        char_set.add(s[end]) 
        current_length = end - start + 1
        if current_length > max_length:
            max_length = current_length 
            longest_substring = s[start:end+1]

    return longest_substring, max_length

# Example usage:
s = "abcabcbb"
longest_substring, length = longest_unique_substring(s)
print(f"The longest substring without repeating characters is: '{longest_substring}' with length {length}")
"""
# Given a string s, reverse the string without reversing its individual words. Words are separated by dots(.).

# Note: The string may contain leading or trailing dots(.) or multiple dots(.) between two words. The returned string should only have a single dot(.) separating the words, and no extra dots should be included.

# Examples :

# Input: s = "i.like.this.program.very.much"
# Output: "much.very.program.this.like.i"
#method1
def reverseWords(s):
    words=s.split(".")
    words=[word for word in words if word]
    return ".".join(words[::-1])

s="i.like.this.program.very.much"
print(reverseWords(s))

#method2
s="i.like.this.program.very.much"
words=[]
word=""
for char in s:
    if char==".":
        if word!="":
            words.append(word)
            word=""
    else:
        word+=char
if word!="":
    words.append(word)
result=""
for i in range(len(words)-1,-1,-1):
    result+=words[i]
    if i!=0:
        result+="."
print(result)


def non_repeate(s):
    n=len(s)  
    for i  in range(n):
        found=False
        for j in range(n):
            if i!=j and s[i]==s[j]:
                found=True
                break
        if not found:
            return s[i]
    return '$'
    
s="GeeksForGeeks"
res=non_repeate(s)
print(res)

#first repeating chars
#method1
class Solution:
    def firstRepChar(self, s):
        seen=set()
        for char in s:
            if char in seen:
                return char
            seen.add(char)

        return #


s = "geeksforgeeks"

s1 = Solution()
print(s1.firstRepChar(s)) 


#method2
class Solution:
    def firstRepChar(self, s):
        n = len(s)

        for i in range(1, n):
            for j in range(i):
                if s[i] == s[j]:
                    return s[i]

        return '#'


s = "geeksforgeeks"

s1 = Solution()
print(s1.firstRepChar(s)) 