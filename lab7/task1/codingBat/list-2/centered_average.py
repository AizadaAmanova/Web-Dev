def centered_average(nums):
    total_sum = sum(nums)
    max_val = max(nums)
    min_val = min(nums)
    centered_sum = total_sum - max_val - min_val
    
    return centered_sum // (len(nums) - 2)