alist = ["a", "c", "d", "f", "f", "h", "t"]

def find(alist, val, left, right):
    if (right - left) <= 1:
        if val == alist[left]:
            return True
        elif val == alist[right]:
            return True    
        else:
            return False
    vysledek = alist[(left+right)//2]
    if vysledek == val:
        return True
    elif vysledek < val:
        left = (left+right)//2
    elif vysledek > val:
        right = (left+right)//2
    find(alist, val, left, right)
    

print(find(alist, 'h', 0, len(alist)))