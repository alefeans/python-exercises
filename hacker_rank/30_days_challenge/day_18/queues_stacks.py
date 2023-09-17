#!/usr/bin/python3


class Solution:
    # Write your code here
    def __init__(self):
        self.queue = []
        self.stack = []

    def pushCharacter(self, s):
        self.stack.append(s)

    def popCharacter(self):
        return self.stack.pop()

    def enqueueCharacter(self, s):
        self.queue.append(s)

    def dequeueCharacter(self):
        return self.queue.pop(0)


# read the string s
s = input()
# Create the Solution class object
obj = Solution()

length = len(s)
# push/enqueue all the characters of string s to stack
for i in range(length):
    obj.pushCharacter(s[i])
    obj.enqueueCharacter(s[i])

isPalindrome = True
"""
pop the top character from stack
dequeue the first character from queue
compare both the characters
"""
for i in range(length // 2):
    if obj.popCharacter() != obj.dequeueCharacter():
        isPalindrome = False
        break
# finally print whether string s is palindrome or not.
if isPalindrome:
    print("The word, " + s + ", is a palindrome.")
else:
    print("The word, " + s + ", is not a palindrome.")
