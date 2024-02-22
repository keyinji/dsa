def recursive_binary(target, list):
    if len(list) == 0:
        return False
    else: 
        midpoint = (len(list))//2
        if list[midpoint] == target:
            return midpoint
        else:
            if list[midpoint] < target:
                return recursive_binary(target, list[midpoint+1:])
            else:
                return recursive_binary(target, list[:midpoint])

numbers = [1,2,3,4,5,6,7,8,9,10]

def verify(index):
    if index is not None:
        print("Target found at: ", index)
    else:
        print("Target not found in list") 
        
        
verify(recursive_binary(12, numbers))
verify(recursive_binary(6, numbers))