def array_front9(nums):
  count = 0
  for i in range(len(nums)):
    if nums[i] == 9 and i<= 3:
      count += 1
  return bool(count)
      
      
