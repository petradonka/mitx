''' CORRECT
Assume s is a string of lower case characters.

Write a program that prints the longest substring of s in which 
the letters occur in alphabetical order.
For example, if s = 'azcbobobegghakl', then your program should print

    Longest substring in alphabetical order is: beggh

In the case of ties, print the first substring. 
For example, if s = 'abcbcd', then your program should print

    Longest substring in alphabetical order is: abc

'''
#s = 'azcbobobegghaklbeggh'
s = 'azcbobobegghaklbegghabcdefghijklmnopqrstuvwxyzbegghazcbobobegghaklbeggh'
#s = 'hmsvxdchxxrsyj'

###

index = 0
current_streak = ''
streaks = []

def alphabetIndex(char):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    return alphabet.index(char) 

for char in s:
    char_index = alphabetIndex(char) 
    if index > 0:
        prev_char = s[index-1]
    else:
        prev_char = ''
        
    prev_char_index = alphabetIndex(prev_char)
    
    if char_index >= prev_char_index:
        if len(current_streak) == 0:
            current_streak = current_streak + prev_char
        current_streak = current_streak + char
    else:
        if len(current_streak) == 0:
            current_streak = current_streak + prev_char
        streaks.append(current_streak)
        current_streak = ''    
    
    if ((len(current_streak) > 0) and (index == (len(s)-1))):
        streaks.append(current_streak)
    
    index += 1

longest_streak = ''
streak_index = 0

for streak in streaks:
    if (((len(streak) > len(longest_streak)))):
        longest_streak = streak
    streak_index += 1
    
print "Longest substring in alphabetical order is: " + longest_streak