# Returns the majority element in a list. A majority element is defined as any element which occurs in the list more than n/2 times,
# where n is the number of elements. Returns -1 if there is no majority element. 


def get_majority_element(a, left, right):
 
    if left == right:
        return -1
    if left + 1 == right:
        return a[left]
    # Conquer
    # Divide
    mid = (left+right)//2 
    leftSide = get_majority_element(a, left, mid)
    rightSide = get_majority_element(a,mid,right)
    # Conquer
    if leftSide == rightSide:
        majority = leftSide
        return majority
    if leftSide == -1 and rightSide == -1:
        return -1
    else:
        l = a[left:mid]
        r = a[mid:right]
        lst = l+r        
        if lst.count(leftSide) > len(lst) //2:
            return leftSide
        if lst.count(rightSide) > len(lst)//2:
            return rightSide
        else:
            return -1
            

