def NarcissisticNumber(n):
    '''
    https://www.codewars.com/kata/5287e858c6b5a9678200083c
    6 kyu
    '''
    nstr = str(n)
    power = len(nstr)
    
    answer = 0
    for i in nstr:
        answer = answer + int(i) ** power
           
    if answer == n:
        return True
    else:
        return False