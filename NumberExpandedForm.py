def expanded_form(num):
    '''
    https://www.codewars.com/kata/5842df8ccbd22792a4000245
    6 kyu
    '''
 
    #define variables
    numstr = str(num)    
    length = len(numstr)
    list = []
    
    #iterate through number and add digits to list
    for i in numstr:
        x = int(i) * 10 ** (length-1)
        if x != 0:
            list.append(str(x))
        length -= 1
        
    #return the list in desired form   
    answer = ' + '.join(list)
    return answer