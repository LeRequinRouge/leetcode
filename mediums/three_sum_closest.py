num_list = [7, 9, -1, 4]
num_list.sort()
target = 1


def three_sum_closest(nums, targ):
    sum_list = []
    closest_sum = 1000

    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        j = i + 1
        k = len(nums) - 1

        while j < k:
            three_sum = nums[i] + nums[j] + nums[k]
            sum_list.append(three_sum)

            if three_sum == targ:
                return targ
            elif three_sum < targ:
                j += 1
            else:
                k -= 1

    closest_sum = min(sum_list, key=lambda x: abs(x - targ))

    return closest_sum


print(three_sum_closest(num_list, target))