def sum67(nums):
    total = 0
    record = True
    
    for num in nums:
        if num == 6:
            record = False
        
        if record:
            total += num
            
        if num == 7 and not record:
            record = True
            
    return total