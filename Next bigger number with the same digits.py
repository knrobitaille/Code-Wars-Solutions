def next_bigger(n):
    """
    https://www.codewars.com/kata/55983863da40caa2c900004e
    4 kyu
    
    After a few close but failed attempts, I used the following post to help work through the problem:
    
        https://medium.com/@destefanoflavio/kata-resolution-next-bigger-number-with-the-same-digits-4eab491852d2
    
    As the post explains, you can break out the number into left, right, and pivot variables
    Pivot is the digit(going right to left) that is less than the previous digit
    Right are the numbers to the right of the pivot, and left are the numbers to the left
    The pivot is then swapped with the lowest number from the right group that is > the pivot
    The right (with the pivot swapped in) is then sorted
    To get the final answer just concatenate the left, switched number, and new right!
    """
    #print("Number:",n)
    
    # Set up variables
    left = ''
    right = ''
    pivot = ''
    
    # Turn input into string and reverse for 'right to left' traversal
    rev_n = str(n)[::-1]
    #print("Reversed:",rev_n)
    
    # Iterate through reversed string
    for i in range(len(rev_n)-1):
        # Check current index vs next, looking for current to be greater than next
        if int(rev_n[i])>int(rev_n[i+1]):
            
            # Set pivot
            pivot = str(rev_n[i+1])
            #print("Pivot:",pivot)
            
            # Set left
            left = rev_n[i+2:]
            left = left[::-1]
            #print("Left:",left)
            
            # Set right
            right = rev_n[:i+1]
            right = right[::-1]
            #print("Tight:",right)
            
            # Break out of loop because pivot was found
            break
        
    # If no pivot is found then there is no solution for this input, return -1    
    if pivot == '':
        return -1
    
    # Set up switch variable which will be swapped with the pivot 
    switch = 10
    # Iterate through right variable
    for i in right:
        # Looking for smallest number that is greater than the pivot
        if int(i) > int(pivot) and int(i) < int(switch):
            switch = i
    #print("Switch:",switch)
    
    # Find new right, which swaps the switch var for the pivot and is then sorted
    new_right = right.replace(str(switch),pivot,1)
    new_right = ''.join(sorted(new_right))
    #print("New right:",new_right)
    
    # Concatenate the left, switch, and new right for the answer
    answer = int(left+str(switch)+new_right)
    #print("Answer:",answer)
    return answer


# print(next_bigger(12))
# print(next_bigger(513))
# print(next_bigger(2017))
# print(next_bigger(414))
# print(next_bigger(144))
# print(next_bigger(9876543210))
# print(next_bigger(21581957621))