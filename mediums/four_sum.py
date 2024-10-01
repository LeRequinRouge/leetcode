nums_list = [-3, -1, 0, 2, 4, 5]
target_int = 0


def four_sum(nums, target):
    nums.sort()
    temp_list = []
    quad_list = []

    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        j = i + 1
        x = len(nums) - 1
        k = x - 1

        while x > i:
            while j < k:
                temp_list = [nums[i], nums[j], nums[k], nums[x]]
                sum_total = nums[i] + nums[j] + nums[k] + nums[x]

                if sum_total == target and temp_list not in quad_list:
                    quad_list.append(temp_list)
                    j += 1
                elif sum_total < target:
                    j += 1
                else:
                    k -= 1
                    if nums[k] == nums[k + 1]:
                        k -= 1
            j = i + 1
            x -= 1
            k = x - 1

    return quad_list


print(four_sum(nums_list, target_int))


