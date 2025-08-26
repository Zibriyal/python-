#apalindrome if reverse  of 'ABBA' is same as 'ABBA'

s=input('Enter a string: ')
low=0
high=len(s)-1
while low<high:
    if s[low]!=s[high]:
        print('Not palindrome')
        break
    low+=1
    high-=1
else:
    print('Palindrome')

# Second shortcut method by reverse slicing

s=input('Enter a string: ')
if s==s[::-1]:
    print('Palindrome')
else:
    print('Not palindrome')
