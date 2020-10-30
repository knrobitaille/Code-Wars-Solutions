'''
https://www.codewars.com/kata/59c633e7dcc4053512000073
6 kyu
'''
def solve(s):
    
    # set variables
    vowels = ['a','e','i','o','u']
    consonant_substrings = []
    
    # find consonant substrings
    for n, ch in enumerate(s):
        curr_string = ''
        count = n
        while s[count] not in vowels:
            curr_string += s[count]
            count += 1
            if count == len(s):
                break
        consonant_substrings.append(curr_string)
    
    # find highest value of consonant substrings
    highest_value = 0
    for i in consonant_substrings:
        current_value = 0
        for l in i:
            current_value += ord(l)-96
        if current_value > highest_value:
            highest_value = current_value
    
    # return highest value
    return highest_value