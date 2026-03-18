def max_end3(nums):
  if (nums[0] > nums[-1]):
    for i in range(len(nums)) :
      nums[i] = nums[0]
  else:
    for i in range(len(nums)) :
      nums[i] = nums[-1]
  return nums
