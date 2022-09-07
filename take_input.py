import re

def add(string):
    if len(string) == 0:
        return 0
    

    lst = re.split(',|\n', string)
    ans = 0
    neg = []
    for item in lst:
        if(item >= 'a' and item <= 'z'):
            ans += (ord(item) - ord('a')) + 1

        elif int(item) < 0:
            neg.append(int(item))

        elif int(item) <= 1000:
            ans += int(item)
    
    if len(neg) > 0:
        raise Exception("Negatives not allowed", neg)

    return ans

