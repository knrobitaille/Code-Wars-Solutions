def encode(s):
    """
    Part 1
    https://www.codewars.com/kata/5d617c2fa5e6a2001a369da2
    4 kyu
    """
    # Create list of lists
    all_list = []
    # Enumerate through string
    for n,i in enumerate(s):
        cur_list = []
        x = n
        # Add a list for each time through
        # List starts at next index each time and puts whole string into list
        while len(cur_list) < len(s):
            cur_list.append(s[x])
            x+=1
            # reset to 0 index after passing last index
            if x > len(s)-1:
                x = 0
        # Add current list to main list of lists
        all_list.append(cur_list)
    # Print final matrix (list of lists)
    # print(all_list)
    
    # Set up to find answer
    answer_word = ''
    answer_num = 0
    # Enumerate through sort final matrix
    for n, lst in enumerate(sorted(all_list)):
        # Add last letter of each row to answer_word
        answer_word += lst[len(s)-1]
        # If row equals word, store that index in answer_num
        if s == "".join(lst):
            answer_num=n
    # Return answer word and answer num
    return(answer_word,answer_num)

def decode(s, n):
    """
    Part 2
    https://www.codewars.com/kata/5d617c2fa5e6a2001a369da2
    4 kyu
    
    I relied on this video a lot for help
    https://www.youtube.com/watch?v=fwADdeurjTE
    I used many videos and resources but this was the one where it clicked
    """
    # Check for valid input
    # From what I could tell CodeWars only tested valid input on decode, not on encode
    if n < 0 or n > len(s) or s == '':
        return ''
    
    # Create empty list
    table = [''] * len(s)

    # Iterate based on length of input
    for i in range(len(s)):
        # Iterate again for each string in list
        for x in range(len(s)):
            # Set value equal current value plus string value at same index
            table[x] = s[x]+table[x]
        # Sort table before iterating through again
        table = sorted(table)
    # Once table is finished, return based on index input
    return table[n]

# print(encode("bananabar"))
# print(decode("nnbbraaaa", 4))
# print(encode("Humble Bundle"))
# print(decode("e emnllbduuHB", 2))