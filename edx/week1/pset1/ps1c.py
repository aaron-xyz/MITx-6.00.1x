# both substrings start with the first char of the string s
longest_sub = s[0]
sub = s[0]

# Store the length of the longest substring
longest_len = len(longest_sub)

for index in range(1,len(s)):
	# check if the string is in alphabetical order
    if s[index] >= s[index-1]:
    	# append that char to the current substring
        sub += s[index]
        sub_len = len(sub)
        # if the substring becomes the largest substring then ...
        if longest_len < sub_len:
        	longest_sub = sub
    else:
    	# update the length of the longest substring
        longest_len = len(longest_sub)
        sub = s[index]
print("Longest substring in alphabetical order is: " + longest_sub)
