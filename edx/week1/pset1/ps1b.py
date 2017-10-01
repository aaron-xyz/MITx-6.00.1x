s = 'azcbobobegghakl'
count_bob = 0

# Search bobs
while True:
    if 'bob' in s:
        count_bob += 1
        index = s.index('bob')
        s = s[index+1:]
    else:
        break
print("Number of times bob occurs is: " + str(count_bob))
