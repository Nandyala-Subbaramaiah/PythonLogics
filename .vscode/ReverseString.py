#String Reverse Pogramming
str="subbu is python developer"
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

s='AABBSDAG'
s2=set(s)
Output=''.join(s2)
print(Output)

s='AABBSDAG'
s2=set(s)
Output=''.join(s2)
print(Output)

