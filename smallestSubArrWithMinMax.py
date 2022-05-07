def subArrWithMinMaxValue(nums):
	if len(nums) < 3:
		return nums

	identifier = nums[0] < nums[1]
	minInd = startIndex  = 0
	maxInd = endIndex = len(nums) - 1
	maxDiff = 0
	result = []

	for index in range(len(nums) - 1):
		if identifier and nums[index] >= nums[index + 1]:
			result.append([startIndex, endIndex])
			startIndex = index
			identifier = 0
		if not identifier and nums[index] <= nums[index + 1]:
			result.append([startIndex, endIndex])
			startIndex = index
			identifier = 1
		if not identifier and nums[index] >= nums[index + 1]:
			endIndex = index + 1
		if identifier and nums[index] <= nums[index + 1]:
			endIndex = index + 1

	result.append([startIndex, endIndex])
	for item in result:
		if maxDiff < abs(nums[item[0]] - nums[item[1]]) or \
				(maxDiff == abs(nums[item[0]] - nums[item[1]]) \
				and abs(item[0] - item[1]) <= abs(maxInd - minInd)):
			maxDiff = abs(nums[item[0]] - nums[item[1]])
			minInd = item[0]
			maxInd = item[1]


	return nums[minInd: maxInd + 1]
