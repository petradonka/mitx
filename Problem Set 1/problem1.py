''' s = lowercase string '''
s = 'azcbobobegghakl'
''' => Number of vowels: 5 '''

vowels = 'aeiou'
vowel_count = 0
for char in s:
    if char in vowels:
        vowel_count += 1
        
print ("Number of vowels: " + str(vowel_count))

''' correct '''