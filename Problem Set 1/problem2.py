''' s = lowercase string '''
s = 'azcbobobegghakl'
''' => Number of times bob occurs is: 2 '''

index = 0
bob_count = 0
for char in s:
    if char == 'b':
        if ('bob' in s[index:index+3]):
            bob_count += 1
    index += 1
        
print "Number of times 'bob' occurs is: " + str(bob_count)

''' correct '''